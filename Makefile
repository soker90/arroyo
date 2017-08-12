all: install

install:
	mkdir -p /usr/share/arroyo/default/
	mkdir -p /usr/share/arroyo/resources/
	cp -r src /usr/share/arroyo/
	cp -r ui /usr/share/arroyo/
	cp default/database.sql /usr/share/arroyo/default/
	cp resources/arroyo.desktop /usr/share/applications/
	cp resources/logo.png /usr/share/pixmaps/arroyo.png
	cp resources/arroyo /usr/bin/
	chmod +x /usr/bin/arroyo

uninstall:
	rm -rf /usr/share/arroyo/
	rm /usr/share/applications/arroyo.desktop
	rm /usr/share/pixmaps/arroyo.png
	rm /usr/bin/arroyo

clean:
	rm -rf src/__pycache__
	rm -rf src/lib/__pycache__
