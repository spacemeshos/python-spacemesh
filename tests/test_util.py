from ..transactions import signer_from_seed, TransactionBody, GeneralTransaction

alice = signer_from_seed("alice")
bob = signer_from_seed("bob")


def assert_equal_tx_body(a: TransactionBody, b: TransactionBody):
    assert a.get_ttl() == b.get_ttl()
    assert a.get_recipient() == b.get_recipient()
    assert a.get_nonce() == b.get_nonce()
    assert a.get_gas_limit() == b.get_gas_limit()
    assert a.get_gas_price() == b.get_gas_price()


def assert_equal_tx(a: GeneralTransaction, b: GeneralTransaction):
    assert a.tx_type == b.tx_type
    assert_equal_tx_body(a.body, b.body)
