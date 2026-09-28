/* from gettext-tiny; to fool configure scripts generated with old gettext.m4
 * to properly use musl's builtin intl funcs (as these internal symbols may be
 * checked)
 */

const char *_nl_expand_alias () { return 0; }
int _nl_msg_cat_cntr = 0;
