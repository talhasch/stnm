import unittest

from stnm.cli.config import config_input_parser, InvalidConfigEntry, UnavailableConfigParameter, InvalidValue


class ConfigTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.maxDiff = 1000

    def test_parse_01(self):
        resp = config_input_parser("node.miner=true,node.seed=True,burnchain.peer_port=2000,node.seed=abccd1df")
        self.assertEqual(str(resp), "[<node.miner=True>, <node.seed=True>, <burnchain.peer_port=2000>, <node.seed=abccd1df>]")

    def test_parse_invalid_entry_02(self):
        with self.assertRaises(InvalidConfigEntry) as ctx:
            config_input_parser("foo")

        self.assertEqual("InvalidConfigEntry" in str(type(ctx.exception)), True)

        with self.assertRaises(InvalidConfigEntry) as ctx:
            config_input_parser("foo.bar")

        self.assertEqual("InvalidConfigEntry" in str(type(ctx.exception)), True)

    def test_parse_unavailable_config_parameter_03(self):
        with self.assertRaises(UnavailableConfigParameter) as ctx:
            config_input_parser("foo.bar=baz")

        self.assertEqual("UnavailableConfigParameter" in str(type(ctx.exception)), True)

    def test_parse_invalid_value_04(self):
        with self.assertRaises(InvalidValue) as ctx:
            config_input_parser("node.miner=12")

        self.assertEqual("InvalidValue" in str(type(ctx.exception)), True)
