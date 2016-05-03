.PHONY: builddeb
builddeb:
	dpkg-buildpackage -us -uc
