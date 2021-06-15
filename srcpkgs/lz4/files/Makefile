VERSION = 1.9.3
CC     ?= cc
CFLAGS ?= -O2
PREFIX ?= /usr/local
LIBDIR ?= $(PREFIX)/lib
INCDIR ?= $(PREFIX)/include
MANDIR ?= $(PREFIX)/share/man/man1
PCDIR  ?= $(LIBDIR)/pkgconfig
EXTRA_CFLAGS = -Ilib -fPIC -fvisibility=hidden -DXXH_NAMESPACE=LZ4_ \
	-Wall -Wextra -Wcast-qual -Wcast-align -Wshadow -Wswitch-enum \
	-Wdeclaration-after-statement -Wstrict-prototypes \
	-Wundef -Wpointer-arith -Wstrict-aliasing=1

LIB_OBJS = lib/lz4.o lib/lz4frame.o lib/lz4hc.o lib/xxhash.o
BIN_OBJS = programs/bench.o programs/datagen.o programs/lz4cli.o programs/lz4io.o

SONAME = liblz4.so.1

all: liblz4.pc liblz4.a liblz4.so.$(VERSION) $(BIN_OBJS)
	$(CC) $(EXTRA_CFLAGS) $(CFLAGS) $(LDFLAGS) \
		$(LIB_OBJS) $(BIN_OBJS) -o lz4

.c.o:
	$(CC) -c -o $@ $< $(EXTRA_CFLAGS) $(CFLAGS)

liblz4.a: $(LIB_OBJS)
	ar rcs liblz4.a $(LIB_OBJS)

liblz4.so.$(VERSION): $(LIB_OBJS)
	$(CC) $(EXTRA_CFLAGS) $(CFLAGS) $(LDFLAGS) -Wl,-soname=$(SONAME) \
		-shared -o liblz4.so.$(VERSION)

liblz4.pc: lib/liblz4.pc.in
	sed -e "s,@PREFIX@,$(PREFIX),g" \
		-e "s,@LIBDIR@,$(LIBDIR),g" \
		-e "s,@INCLUDEDIR@,$(INCDIR),g" \
		-e "s,@VERSION@,$(VERSION),g" \
		lib/liblz4.pc.in > liblz4.pc

install:
	install -Dm755 lz4 $(DESTDIR)$(PREFIX)/bin/lz4
	install -Dm644 programs/lz4.1 $(DESTDIR)$(MANDIR)/lz4.1

	install -Dm644 liblz4.a $(DESTDIR)$(LIBDIR)/liblz4.a
	install -Dm755 liblz4.so.$(VERSION) $(DESTDIR)$(LIBDIR)/liblz4.so.$(VERSION)

	install -Dm644 liblz4.pc $(DESTDIR)$(PCDIR)/liblz4.pc

	install -Dm644 lib/lz4hc.h $(DESTDIR)$(INCDIR)/lz4hc.h
	install -Dm644 lib/lz4frame_static.h $(DESTDIR)$(INCDIR)/lz4frame_static.h
	install -Dm644 lib/lz4frame.h $(DESTDIR)$(INCDIR)/lz4frame.h
	install -Dm644 lib/lz4.h $(DESTDIR)$(INCDIR)/lz4.h

	ln -sf liblz4.so.$(VERSION) $(DESTDIR)$(LIBDIR)/$(SONAME)
	ln -sf liblz4.so.$(VERSION) $(DESTDIR)$(LIBDIR)/liblz4.so
	ln -sf lz4 $(DESTDIR)$(PREFIX)/bin/lz4c
	ln -sf lz4 $(DESTDIR)$(PREFIX)/bin/lz4cat
	ln -sf lz4 $(DESTDIR)$(PREFIX)/bin/unlz4
	ln -sf lz4.1 $(DESTDIR)$(MANDIR)/lz4c.1
	ln -sf lz4.1 $(DESTDIR)$(MANDIR)/lz4cat.1
	ln -sf lz4.1 $(DESTDIR)$(MANDIR)/unlz4.1
