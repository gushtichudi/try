all: @echo "Please run sudo make install to install this Python script to your UNIX-Like machine."

install:
	install -m755 try.py /usr/local/bin/try

uninstall:
	rm -rf /usr/local/bin/try
