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

// Hangs sending pings on stop sometimes and prevents FF close
pref("toolkit.telemetry.shutdownPingSender.enabled", false);

// ad shit
pref("dom.private-attribution.submission.enabled", false);
