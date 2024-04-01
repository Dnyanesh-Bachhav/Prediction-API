import ada
import bch
import bit
import doge
import dot
import eth
import ltc
import shib
import usdt
import xlm


def get_prediction(crypto):
    if crypto == "BTC":
            print("bitcoin")
            data = bit.get_bit()
            return data
    if crypto == "ETH":
            data = eth.get_eth()
            return data
    if crypto == "XLM":
            data = xlm.get_xlm()
            return data
    if crypto == "USDT":
            data = usdt.get_usdt()
            return data
    if crypto == "BCH":
            data = bch.get_bch()
            return data
    if crypto == "LTC":
            data = ltc.get_ltc()
            return data
    if crypto == "PDOT":
            data = dot.get_dot()
            return data
    if crypto == "DOGE":
            data = doge.get_doge()
            return data
    if crypto == "ADA":
            data = ada.get_ada()
            return data
    if crypto == "SHIB":
            data = shib.get_shib()
            return data

