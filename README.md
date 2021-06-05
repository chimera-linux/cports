# cports

Cports is a collection of source package ports for Chimera. It was originally
created as a rewrite of `xbps-src` from Void Linux in Python. Currently it is
still somewhat messy, and still uses xbps, and does not yet have a complete
bootstrap collection. This is, however, going to change in very near future.

## TODO

Right now it is very limited. It is capable of creating packages, but it cannot
properly build dependencies and most commands are missing.

* Dependency building
* Cross-compiling
* Clean, bootstrap update, etc.
* Complete bootstrap collection
* Rebase on Clang
* Move away from xbps
* ...
