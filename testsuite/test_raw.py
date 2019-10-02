# -*- coding: utf-8 -*-

import os
import unittest

from ton_client.client import TonlibClientFutures

proj_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..')


class ClientOnlineTestCase(unittest.TestCase):
    def test_raw_getaccount_state(self):
        t = TonlibClientFutures()
        ft = t.raw_get_account_state('-1:DD74DD3DA6E2AC5A5A090875BD08D3F8E61388BD200AA7BBC70957640D732236')
        res = ft.result()
        self.assertIsInstance(res, dict)
        self.assertEqual('raw.accountState', res['@type'])

    def test_raw_get_transactions(self):
        t = TonlibClientFutures()
        ft = t.raw_get_transactions(
            '-1:DD74DD3DA6E2AC5A5A090875BD08D3F8E61388BD200AA7BBC70957640D732236',
            '466495000001',
            '34A9E5FA0C3F3C4CCCE04013F6D80EE5EC4EC882C0DEF17FBC6C89DFD8E97B15'
        )
        res = ft.result()
        self.assertIsInstance(res, dict)
        self.assertEqual('raw.transactions', res['@type'])

    def test_raw_send_boc(self):
        t = TonlibClientFutures()
        ft = t.raw_send_boc('B5EE9C724104020100000000A90001CF89FFBAE9BA7B4DC558B4B41210EB7A11A7F1CC27117A40154F778E12AEC81AE6446C003219C84E5B04B5AE35ACCF717469539F4AB34623CC3BA9C980E1F620487F0E29CC03FA0A68A6A53E78CB4DC877454AE9DD74561BDA8CFD95069E67632A91C070000000101C010078427FBE2D02C6134ABBBF7CEB0CF1B6ED7630E39606557084BB72836CFEADFA96163521DCD6500000000000000000000000000000000000005445535414557A60')
        res = ft.result()
        self.assertIsInstance(res, dict)
        self.assertEqual('ok', res['@type'])
