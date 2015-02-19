Feature: creating an invoice
  The user won't get any money 
  If they can't
  Create Invoices

  Background:
    Given the user is authenticated with BitPay

  Scenario Outline: The request is correct
    When the user creates an invoice for <price> <currency> with float input
    Then they should recieve an invoice in response for <price> <currency>
  Examples:
    | price | currency |
    | 5.23  | USD      |
    | 10.21 | EUR      |
    | 0.231 | BTC      |

  Scenario Outline: The request is correct
    When the user creates an invoice for <price> <currency> with integer input
    Then they should recieve an invoice in response for <price> <currency>
  Examples:
    | price | currency |
    | 10    | USD      |

  Scenario Outline: The request is correct
    When the user creates an invoice for <price> <currency> with string input
    Then they should recieve an invoice in response for <price> <currency>
  Examples:
    | price | currency |
    | 5.23  | USD      |
    | 10.21 | EUR      |
    | 10    | USD      |

  Scenario Outline: The invoice contains illegal characters
    When the user creates an invoice for <price> <currency> with string input
    Then they will receive a BitPayArgumentError matching <message>
  Examples:
    | price | currency | message                            |
    | 5,023 | USD      | Price must be formatted as a float |
    | 3.21  | EaUR     | Currency is invalid.               |
    | ""    | USD      | Price must be formatted as a float |
    | Ten   | USD      | Price must be formatted as a float |
    | 10    | ""       | Currency is invalid.               |

