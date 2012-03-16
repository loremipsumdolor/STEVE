'''
S.T.E.V.E. Message Parser
Parses messages for commands
A software component of S.T.E.V.E. (Super Traversing Enigmatic Voice-commanded Engine)
Device invented by Jacob Turner
Code by Squared Pi Productions/Jacob Turner; released under the MIT license
'''

from email import message_from_string
import parsers.cmdparser as cmdparser

class msgparse():
    def __init__(self):
        self.basic = cmdparser.basiccmd()
        self.api = cmdparser.apicmd()

    def interpret(self, data, format):
        if format == "email":
            var = []
            self.body = message_from_string(data)
            self.payload = self.body.get_payload()
            if type(self.payload) is not str:
                self.parsedmsg = self.payload[0].get_payload()
            var.append(self.parsedmsg)
            var.append(self.body["Return-Path"].strip("<>"))
            return var
        elif format == "txt":
            var = []
            var.append(self.data[0])
            var.append(self.data[1])
            return var
        else:
            return "Error: Input not in understandable format."

    def parse(self, data, sender, format):
        var = []
        if data.find("steve picture") != -1:
            self.basic.picture()
            if format == "email":
                var.append("attach")
                var.append("image.jpg")
                var.append(sender)
            elif format == "txt":
                var.append("Image taken successfully.")
                var.append(sender)
            return var
        elif data.find("steve shutdown") != -1:
            self.basic.shutdown()
        elif data.find("steve restart") != -1:
            self.basic.restart()
        elif data.find("steve search") != -1:
            self.term = data.split(" ")
            self.search = self.api.search(self.term[2])
            if format == "email":
                var.append("text")
                for x in self.search:
                    var.append(x)
                var.append(sender)
            elif format == "txt":
                var.append(" ".join(self.search))
                var.append(sender)
            return var
        elif data.find("steve shorten") != -1:
            self.term = data.split(" ")
            self.url = self.api.shorten(self.term[2])
            if format == "email":
                var.append("text")
                var.append(self.url)
                var.append(sender)
            elif format == "txt":
                var.append(self.url)
                var.append(sender)
            return var
        elif data.find("steve ghuser") != -1:
            self.term = data.split(" ")
            self.info = self.api.ghuser(self.term[2])
            if format == "email":
                var.append("text")
                for x in self.info:
                    var.append(x)
                var.append(sender)
            elif format == "txt":
                var.append(" ".join(self.info))
                var.append(sender)
        elif data.find("steve ghproj") != -1:
            self.term = data.split(" ")
            self.info = self.api.ghproj(self.term[2])
            if format == "email":
                var.append("text")
                for x in self.info:
                    var.append(x)
                var.append(sender)
            elif format == "txt":
                var.append(" ".join(self.info))
                var.append(sender)
            return var
        elif data.find("steve weather") != -1:
            self.term = data.split(" ")
            self.info = self.api.weather(self.term[2], self.term[3])
            if format == "email":
                var.append("text")
                for x in self.info:
                    var.append(x)
                var.append(sender)
            elif format == "txt":
                var.append(" ".join(self.info))
                var.append(sender)
            return var
        elif data.find("steve currency") != -1:
            self.term = data.split(" ")
            self.info = self.api.currency(self.term[2], self.term[3])
            if format == "email":
                var.append("text")
                for x in self.info:
                    var.append(x)
                var.append(sender)
            elif format == "txt":
                var.append(" ".join(self.info))
                var.append(sender)
            return var
        else:
            return

if __name__ == '__main__':
    print "Not to be called directly."