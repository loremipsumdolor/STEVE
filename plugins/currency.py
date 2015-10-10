'''
Currency Converter plugin for S.T.E.V.E.
Code by Jacob Turner; released under the MIT license
'''

'''
        elif data.find("steve currency") != -1 or data.find("currency") != -1:
            term = data.split(" ")
            if format == "email" or format == "text":
                result = currency.currency(term[2], term[3])
            else:
                result = currency.currency(term[1], term[2])
            if format == "email":
                var.append("text")
                var.append(sender)
                var.append(None)
                var.append("$%s is %s %s." % (term[2], result[1],
                           term[3].upper()))
            elif format == "txt":
                var.append(sender)
                var.append("$%s is %s %s." % (term[2], result[1],
                           term[3].upper()))
            elif format == "console":
                var.append("$%s is %s %s." % (term[1], result[1],
                           term[2].upper()))
            return var
'''

import urllib2
import json
import decimal

def currency(amount, new):
    info = json.load(urllib2.urlopen("https://raw.github.com/currencybot/open-exchange-rates/master/latest.json"))
    new = str(decimal.Decimal(decimal.Decimal(amount)*
              decimal.Decimal(info["rates"][new]))
              .quantize(decimal.Decimal('.01'),
              rounding=decimal.ROUND_DOWN))
    return new