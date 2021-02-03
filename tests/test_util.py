from ..transactions import Signer, TransactionBody, GeneralTransaction

alice = Signer.from_seed("alice")
bob = Signer.from_seed("bob")


def assert_equal_tx_body(a: TransactionBody, b: TransactionBody):
    assert a.get_ttl() == b.get_ttl()
    assert a.get_recipient() == b.get_recipient()
    assert a.get_nonce() == b.get_nonce()
    assert a.get_gas_limit() == b.get_gas_limit()
    assert a.get_gas_price() == b.get_gas_price()


def assert_equal_tx(a: GeneralTransaction, b: GeneralTransaction):
    assert a.tx_type == b.tx_type
    assert_equal_tx_body(a.body, b.body)


def assert_transaction_equal_to_body(a: GeneralTransaction):
    assert a.body.get_ttl() == a.ttl
    assert a.body.get_amount() == a.amount
    assert a.body.get_nonce() == a.nonce
    assert a.body.get_gas_limit() == a.gas_limit
    assert a.body.get_gas_price() == a.gas_price
    assert a.body.get_recipient() == a.recipient
    assert a.body.get_fee(1) == a.get_fee(1)
