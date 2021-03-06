# -*- coding: utf-8 -*-

from ranger.gui.displayable import Displayable


class Widget(Displayable):
    """A class for classification of widgets."""

    vcsstatus_symb = {
        'conflict':  ('X', ['vcsconflict']),
        'untracked': ('+', ['vcschanged']),
        'deleted':   ('-', ['vcschanged']),
        'changed':   ('*', ['vcschanged']),
        'staged':    ('*', ['vcsstaged']),
        'ignored':   ('·', ['vcsignored']),
        'sync':      ('√', ['vcssync']),
        'none':      (' ', []),
        'unknown':   ('?', ['vcsunknown']),
    }

    vcsremotestatus_symb = {
        'diverged': ('Y', ['vcsdiverged']),
        'ahead':    ('>', ['vcsahead']),
        'behind':   ('<', ['vcsbehind']),
        'sync':     ('=', ['vcssync']),
        'none':     ('⌂', ['vcsnone']),
        'unknown':  ('?', ['vcsunknown']),
    }

    ellipsis = {False: '~', True: '…'}
