from ..transactions import sign, decode, Address, SimpleCoinTx
from .test_util import alice, bob, assert_equal_tx


def test_simpletx_str():
    ft = SimpleCoinTx(ttl=0, recipient=bob.address, nonce=0, amount=100, gas_limit=2, gas_price=1)
    assert str(ft) == "SimpleCoinTx(ttl=0, nonce=0, recipient=" + \
           str(bob.address) + ", amount=100, gas_limit=2, gas_price=1)"


def test_incomplete_simpletx_str():
    ft = SimpleCoinTx(ttl=0, recipient=bob.address, nonce=0, amount=100, gas_limit=2, gas_price=1)
    ftx = ft.new_ed()
    assert str(ftx) == \
           "IncompleteTransaction(tx_type=SIMPLE_COIN_ED_TX, body=SimpleCoinTx(ttl=0, nonce=0, recipient=" + \
           str(bob.address) + ", amount=100, gas_limit=2, gas_price=1))"


def test_complete_simpletx_str():
    ft = SimpleCoinTx(ttl=0, recipient=bob.address, nonce=0, amount=100, gas_limit=2, gas_price=1)
    tx = sign(ft.new_ed(), alice)
    assert str(tx) == "Transaction(tx_type=SIMPLE_COIN_ED_TX, body=SimpleCoinTx(ttl=0, nonce=0, recipient=" + \
           str(bob.address) + ", amount=100, gas_limit=2, gas_price=1), " + \
           "signature=" + str(tx.signature) + ", " + \
           "public_key=" + str(tx.public_key) + ")"


def test_simple_transaction():
    ft = SimpleCoinTx(ttl=0, recipient=bob.address, nonce=0, amount=100, gas_limit=2, gas_price=1)
    ftx = ft.new_ed()
    stx = ftx.message.sign(alice)
    tx = decode(stx)
    assert_equal_tx(ftx, tx)


cases_signer = alice

case1_tx = SimpleCoinTx(
    ttl=0,
    nonce=5,
    recipient=Address.from_list([
        0x26, 0x4d, 0xd0, 0x80, 0xe4, 0xb3, 0xe7, 0x30, 0x16, 0xbd, 0xf6, 0x57, 0x4b, 0x4c, 0xd8, 0x7e,
        0xaa, 0x69, 0x7f, 0x5e]),
    amount=102,
    gas_limit=1,
    gas_price=10)

case1_signed_ed_tx = bytes([
    # type
    0x00, 0x00, 0x00, 0x00,
    # signature
    0xb0, 0x5b, 0x3e, 0x68, 0x73, 0x57, 0xba, 0x93, 0x17, 0x80, 0x6b, 0xd4, 0x81, 0x43, 0x84, 0x1f, 0xc4, 0xaf, 0x3a,
    0xb0, 0x75, 0xcb, 0xa4, 0xba, 0xe5, 0xe9, 0xb0, 0x74, 0x51, 0x0e, 0x29, 0xc3, 0x6f, 0x9c, 0xc2, 0x5a, 0x33, 0x52,
    0xab, 0xaf, 0xa2, 0x9e, 0x96, 0x9b, 0x51, 0xf5, 0x18, 0xe7, 0x4a, 0x83, 0xda, 0x5b, 0xee, 0xef, 0x5f, 0x52, 0x91,
    0x3f, 0x0d, 0x2c, 0x34, 0x2c, 0x81, 0x07,
    # data
    0x00, 0x00, 0x00, 0x34, 0x00, 0x00, 0x00, 0x00, 0x05, 0x00, 0x00, 0x00, 0x26, 0x4d, 0xd0, 0x80, 0xe4, 0xb3, 0xe7,
    0x30, 0x16, 0xbd, 0xf6, 0x57, 0x4b, 0x4c, 0xd8, 0x7e, 0xaa, 0x69, 0x7f, 0x5e, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x66, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0a,
    # public key
    0x00, 0x00, 0x00, 0x20, 0x38, 0x08, 0x8e, 0x4c, 0x2a, 0xe8, 0x2f, 0x5c, 0x45, 0xc6, 0x80, 0x8a, 0x61, 0xa6, 0x49,
    0x0d, 0x3c, 0x61, 0x2c, 0xe1, 0xda, 0x23, 0x57, 0x14, 0x46, 0x6f, 0xc7, 0x48, 0xfb, 0xc4, 0xcb, 0xbb,
])

case1_signed_edp_tx = bytes([
    # type
    0x01, 0x00, 0x00, 0x00,
    # signature
    0xc8, 0x4a, 0x06, 0x90, 0x0a, 0x04, 0xec, 0x7f, 0x54, 0x46, 0x52, 0xa4, 0xba, 0xd3, 0x88, 0xfb, 0x56, 0x3b, 0x21,
    0xb5, 0x5d, 0x68, 0x33, 0x24, 0xb3, 0xd3, 0xfb, 0xdc, 0x82, 0xa9, 0x91, 0x56, 0x58, 0x8c, 0x45, 0x32, 0xc8, 0x40,
    0xac, 0x3c, 0xb4, 0xb5, 0x59, 0xec, 0x52, 0x17, 0x6e, 0x30, 0x0c, 0x10, 0x8a, 0x6b, 0x21, 0x4d, 0x7c, 0xd1, 0xcc,
    0xb0, 0x92, 0x21, 0x0b, 0x1f, 0xda, 0x0f,
    # data
    0x00, 0x00, 0x00, 0x34, 0x00, 0x00, 0x00, 0x00, 0x05, 0x00, 0x00, 0x00, 0x26, 0x4d, 0xd0, 0x80, 0xe4, 0xb3, 0xe7,
    0x30, 0x16, 0xbd, 0xf6, 0x57, 0x4b, 0x4c, 0xd8, 0x7e, 0xaa, 0x69, 0x7f, 0x5e, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x66, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0a,
])

case2_tx = SimpleCoinTx(
    ttl=0,
    nonce=8,
    recipient=Address.from_list([
        0x26, 0x4d, 0xd0, 0x80, 0xe4, 0xb3, 0xe7, 0x30, 0x16, 0xbd, 0xf6, 0x57, 0x4b, 0x4c, 0xd8, 0x7e, 0xaa, 0x69,
        0x7f, 0x5e]),
    amount=103,
    gas_limit=10,
    gas_price=1)

case2_signed_ed_tx = bytes([
    # type
    0x00, 0x00, 0x00, 0x00,
    # signature
    0x49, 0x7f, 0x2a, 0x0b, 0xba, 0x6f, 0x14, 0xa7, 0x39, 0xec, 0x0e, 0x66, 0x14, 0x2d, 0x5f, 0xda, 0xb1, 0xa1, 0x2e,
    0xd1, 0xba, 0x7b, 0x76, 0x4d, 0x0a, 0xcd, 0x2a, 0x9d, 0xee, 0x05, 0x83, 0xf9, 0xee, 0x6b, 0x87, 0x2a, 0x2e, 0x9c,
    0x06, 0x67, 0x55, 0xf3, 0x1e, 0x14, 0x8a, 0xf9, 0x33, 0x3a, 0xb8, 0x2c, 0xac, 0x9b, 0x83, 0xc2, 0xec, 0xfe, 0x6d,
    0x85, 0xc4, 0x62, 0x06, 0x04, 0x98, 0x02,
    # data
    0x00, 0x00, 0x00, 0x34, 0x00, 0x00, 0x00, 0x00, 0x08, 0x00, 0x00, 0x00, 0x26, 0x4d, 0xd0, 0x80, 0xe4, 0xb3, 0xe7,
    0x30, 0x16, 0xbd, 0xf6, 0x57, 0x4b, 0x4c, 0xd8, 0x7e, 0xaa, 0x69, 0x7f, 0x5e, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x67, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0a, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01,
    # pubkey
    0x00, 0x00, 0x00, 0x20, 0x38, 0x08, 0x8e, 0x4c, 0x2a, 0xe8, 0x2f, 0x5c, 0x45, 0xc6, 0x80, 0x8a, 0x61, 0xa6, 0x49,
    0x0d, 0x3c, 0x61, 0x2c, 0xe1, 0xda, 0x23, 0x57, 0x14, 0x46, 0x6f, 0xc7, 0x48, 0xfb, 0xc4, 0xcb, 0xbb,
])

case2_signed_edp_tx = bytes([
    # type
    0x01, 0x00, 0x00, 0x00,
    # signature
    0x67, 0x21, 0x92, 0x57, 0x76, 0x96, 0x90, 0x70, 0xfd, 0x71, 0xb9, 0x0b, 0x2c, 0x14, 0xb6, 0xe4, 0xfb, 0xda, 0x60,
    0x86, 0xa4, 0x11, 0xaf, 0xb2, 0xba, 0x8d, 0xb4, 0x8d, 0x6d, 0xc5, 0x41, 0xe8, 0x6d, 0xc9, 0xef, 0x35, 0x50, 0xf4,
    0x80, 0x33, 0xea, 0x27, 0x3e, 0xe1, 0x11, 0x1a, 0x3a, 0x98, 0x54, 0xec, 0xaa, 0x7d, 0x7c, 0x51, 0x56, 0xb8, 0xac,
    0x8e, 0xf4, 0xcc, 0xc8, 0xe8, 0xff, 0x05,
    # data
    0x00, 0x00, 0x00, 0x34, 0x00, 0x00, 0x00, 0x00, 0x08, 0x00, 0x00, 0x00, 0x26, 0x4d, 0xd0, 0x80, 0xe4, 0xb3, 0xe7,
    0x30, 0x16, 0xbd, 0xf6, 0x57, 0x4b, 0x4c, 0xd8, 0x7e, 0xaa, 0x69, 0x7f, 0x5e, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x67, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0a, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01,
])

cases = [
    (case1_tx, case1_signed_ed_tx, case1_signed_edp_tx),
    (case2_tx, case2_signed_ed_tx, case2_signed_edp_tx),
]


def test_simpletx_binary_encode():
    for ft, signed_ed, signed_edp in cases:
        tx_ed = ft.new_ed().message.sign(cases_signer)
        assert tx_ed == signed_ed
        tx_edp = ft.new_ed_plus().message.sign(cases_signer)
        assert tx_edp == signed_edp


def test_simpletx_binary_decode():
    for ft, signed_ed, signed_edp in cases:
        tx_ed = decode(signed_ed)
        assert_equal_tx(ft.new_ed(), tx_ed)
        assert tx_ed.origin == cases_signer.address
        tx_edp = decode(signed_edp)
        assert_equal_tx(ft.new_ed_plus(), tx_edp)
        assert tx_edp.origin == cases_signer.address