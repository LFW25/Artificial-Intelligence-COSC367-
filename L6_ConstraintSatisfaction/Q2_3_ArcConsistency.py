# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 17:48:15 2022

@author: lilyw
"""

from csp import *
import itertools

# =============================================================================
# Make the following CSP arc consistent by modifying the code (if necessary)
# 
# from csp import CSP
# 
# crossword_puzzle = CSP(
#     var_domains={
#         # read across:
#         'across1': set("ant big bus car has".split()),
#         'across3': set("book buys hold lane year".split()),
#         'across4': set("ant big bus car has".split()),
#         # read down:
#         'down1': set("book buys hold lane year".split()),
#         'down2': set("ginger search symbol syntax".split()),
#         },
#     constraints={
#         lambda across1, down1: across1[0] == down1[0],
#         lambda down1, across3: down1[2] == across3[0],
#         lambda across1, down2: across1[2] == down2[0],
#         lambda down2, across3: down2[2] == across3[2],
#         lambda down2, across4: down2[4] == across4[0],
#         })
# =============================================================================


crossword_puzzle = CSP(
    var_domains={
        # read across:
        'across1': set("bus has".split()),
        'across3': set("lane year".split()),
        'across4': set("ant car".split()),
        # read down:
        'down1': set("buys hold".split()),
        'down2': set("search syntax".split()),
        },
    constraints={
        lambda across1, down1: across1[0] == down1[0],
        lambda down1, across3: down1[2] == across3[0],
        lambda across1, down2: across1[2] == down2[0],
        lambda down2, across3: down2[2] == across3[2],
        lambda down2, across4: down2[4] == across4[0],
        })


from csp import *
import itertools


# =============================================================================
# canterbury_colouring = CSP(
#     var_domains={
#         'christchurch': {'red', 'green'},
#         'selwyn': {'red', 'green'},
#         'waimakariri': {'red', 'green'},
#         },
#     constraints={
#         lambda christchurch, waimakariri: christchurch != waimakariri,
#         lambda christchurch, selwyn: christchurch != selwyn,
#         lambda selwyn, waimakariri: selwyn != waimakariri,
#         })
# =============================================================================



canterbury_colouring = CSP(
    var_domains={
        'christchurch': {'red', 'green'},
        'selwyn': {'red', 'green'},
        'waimakariri': {'red', 'green'},
        },
    constraints={
        lambda christchurch, waimakariri: christchurch != waimakariri,
        lambda christchurch, selwyn: christchurch != selwyn,
        lambda selwyn, waimakariri: selwyn != waimakariri,
        })