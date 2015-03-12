Feature: pairing with bitpay
  In order to access bitpay
  It is required that the library
  Is able to pair successfully

  Scenario: the client has a correct pairing code
    Given the user pairs with BitPay with a valid pairing code
    Then the user is paired with BitPay

  Scenario: the client initiates pairing
    Given the user requests a client-side pairing
    Then they will receive a claim code

  Scenario Outline: the client has a bad pairing code
    Given the user fails to pair with a semantically <valid> code <code>
    Then they will receive a <error> matching <message>
  Examples:
      | valid   | code     | error                 | message                     |
      | valid   | a1b2c3d  | BitPayBitPayError     | 500: Unable to create token |
      | invalid | a1b2c3d4 | BitPayArgumentError   | pairing code is not legal   |

  Scenario: the client has a bad port configuration to a closed port
    When the user fails to pair with BitPay because of an incorrect port
    Then they will receive a BitPayConnectionError matching Connection refused 

