// Use LANG environment variable to choose locale
pref("intl.locale.requested", "");

// Disable default browser checking.
pref("browser.shell.checkDefaultBrowser", false);

// Don't disable our bundled extensions in the application directory
pref("extensions.autoDisableScopes", 11);
pref("extensions.shownSelectionUI", true);

// Disable some advertising tile garbage on the new tab page
pref("browser.topsites.contile.enabled", false);

// Does not work on musl (proprietary)
pref("media.gmp-widevinecdm.visible", false);
pref("media.gmp-widevinecdm.enabled", false);

// Ditto (crashes)
pref("media.gmp-gmpopenh264.visible", false);
// visible=false means websites that check for it will see it as missing and
// then not try to use it,
// but for some strange reason microsoft teams specifically will then fail
// to load screenshare/video content in calls if it's actually disabled, even
// though it apparently cannot be used. so leave it "enabled"
pref("media.gmp-gmpopenh264.enabled", true);
