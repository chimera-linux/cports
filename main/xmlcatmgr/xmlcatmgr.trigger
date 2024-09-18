#!/bin/sh

set -e

export PATH=/usr/bin

XML_CATALOG=/etc/xml/auto/catalog
SGML_CATALOG=/etc/sgml/auto/catalog

install -d -m 755 /etc/xml/auto
install -d -m 755 /etc/sgml/auto

[ -f "$XML_CATALOG" ] && xmlcatmgr -c "$XML_CATALOG" destroy
[ -f "$SGML_CATALOG" ] && xmlcatmgr -sc "$SGML_CATALOG" destroy

xmlcatmgr -c "$XML_CATALOG" create
xmlcatmgr -sc "$SGML_CATALOG" create

echo "Refreshing XML catalogs..."

if [ ! -f /etc/xml/catalog ]; then
    xmlcatmgr -c /etc/xml/catalog create
fi

if ! xmlcatmgr -c /etc/xml/catalog lookup "$XML_CATALOG" > /dev/null 2>&1; then
    xmlcatmgr -c /etc/xml/catalog add nextCatalog "$XML_CATALOG"
fi

for f in /usr/share/xml/catalogs/*.conf; do
    [ -f "$f" ] || continue
    while read ln; do
        xmlcatmgr -c "$XML_CATALOG" add $ln || echo "failed: $ln"
    done < "$f"
done

echo "Refreshing SGML catalogs..."

if [ ! -f /etc/sgml/catalog ]; then
    xmlcatmgr -sc /etc/sgml/catalog create
fi

if ! xmlcatmgr -sc /etc/sgml/catalog lookup "$SGML_CATALOG" > /dev/null 2>&1; then
    xmlcatmgr -sc /etc/sgml/catalog add CATALOG "$SGML_CATALOG"
fi

for f in /usr/share/sgml/catalogs/*.conf; do
    [ -f "$f" ] || continue
    while read ln; do
        xmlcatmgr -sc "$XML_CATALOG" add $ln || echo "failed: $ln"
    done < "$f"
done
