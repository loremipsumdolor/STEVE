"plugin.py" is an example of how to make a simple
plugin for S.T.E.V.E. However, that is only one of
two parts needed to make the plugin fully-functional,
as the user will need to add a small snippet of code
to addlparser.py for the plugin to return any data.
Below is an example for "plugin.py":

elif data.find("steve helloworld") != -1 or data == "helloworld":
	helloworld()
	if format == "email":
		var.append("text")
		var.append(sender)
		var.append(None)
		var.append("The Hello World app has been executed.")
		return var
	elif format == "txt":
		var.append(sender)
		var.append("The Hello World app has been executed.")
		return var
	elif format == "console":
		return "The Hello World app has been executed."