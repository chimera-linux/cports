#!/bin/sh
#
# this script exists because doing it otherwise would be too ugly :/

set -e

_nsprver=$(pkg-config --modversion nspr)
_nsprver=${_nsprver%.*}

install -d -m 755 ${DESTDIR}/usr/lib/pkgconfig
install -d -m 755 ${DESTDIR}/usr/bin
install -d -m 755 ${DESTDIR}/usr/include/nss

NSS_VMAJOR=$(grep "#define.*NSS_VMAJOR" nss/lib/nss/nss.h | awk '{print $3}')
NSS_VMINOR=$(grep "#define.*NSS_VMINOR" nss/lib/nss/nss.h | awk '{print $3}')
NSS_VPATCH=$(grep "#define.*NSS_VPATCH" nss/lib/nss/nss.h | awk '{print $3}')

sed -e "s,%prefix%,/usr,g" \
    -e 's,%exec_prefix%,${prefix},g' \
    -e 's,%includedir%,${prefix}/include/nss,g' \
    -e 's,%libdir%,${prefix}/lib,g' \
    -e "s,%NSPR_VERSION%,${_nsprver},g" \
    -e "s,%NSS_VERSION%,${NSS_VERSION},g" \
    nss/pkg/pkg-config/nss.pc.in \
    > ${DESTDIR}/usr/lib/pkgconfig/nss.pc

ln -sf nss.pc ${DESTDIR}/usr/lib/pkgconfig/mozilla-nss.pc
chmod 644 ${DESTDIR}/usr/lib/pkgconfig/*.pc

sed -e "s,@prefix@,/usr,g" \
    -e 's,@exec_prefix@,${prefix},g' \
    -e 's,@includedir@,${prefix}/include/nss,g' \
    -e 's,@libdir@,${prefix}/lib,g' \
    -e "s,@MOD_MAJOR_VERSION@,${NSS_VMAJOR},g" \
    -e "s,@MOD_MINOR_VERSION@,${NSS_VMINOR},g" \
    -e "s,@MOD_PATCH_VERSION@,${NSS_VPATCH},g" \
    nss/pkg/pkg-config/nss-config.in \
    > ${DESTDIR}/usr/bin/nss-config
chmod 755 ${DESTDIR}/usr/bin/nss-config

for f in libsoftokn3.so libfreebl3.so libfreeblpriv3.so libnss3.so libnssutil3.so \
    libssl3.so libsmime3.so libnssckbi.so libnssdbm3.so libnsssysinit.so; do
    install -m755 dist/*.OBJ/lib/${f} ${DESTDIR}/usr/lib
done

install -m644 dist/*.OBJ/lib/libcrmf.a ${DESTDIR}/usr/lib

for f in certutil cmsutil crlutil modutil pk12util shlibsign \
    signtool signver ssltap; do
    install -m755 dist/*.OBJ/bin/${f} ${DESTDIR}/usr/bin
done

install -m644 dist/public/nss/*.h ${DESTDIR}/usr/include/nss
