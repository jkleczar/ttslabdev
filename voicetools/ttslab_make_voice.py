#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" This script makes a voice object by loading sub modules and data
    and initialising the appropriate class...

    It looks for specific files and location and should thus be run
    from the appropriate location.
"""
from __future__ import unicode_literals, division, print_function #Py2

__author__ = "Daniel van Niekerk"
__email__ = "dvn.demitasse@gmail.com"

import sys, os

import ttslab

PHONESET_FILE = "phoneset.pickle"
PRONUNDICT_FILE = "pronundict.pickle"
PRONUNADDENDUM_FILE = "pronunaddendum.pickle"
G2P_FILE = "g2p.pickle"
ENGPHONESET_FILE = "engphoneset.pickle"
ENGPRONUNDICT_FILE = "engpronundict.pickle"
ENGPRONUNADDENDUM_FILE = "engpronunaddendum.pickle"
ENGG2P_FILE = "engg2p.pickle"
HTSMODELS_DIR = "data/hts"
USCATALOGUE_FILE = "data/unitcatalogue.pickle"


def usfrontend():
    from ttslab.defaultvoice import LwaziUSVoice
    from ttslab.synthesizer_us import SynthesizerUS
    voice = LwaziUSVoice(phoneset=ttslab.fromfile(PHONESET_FILE),
                         g2p=ttslab.fromfile(G2P_FILE),
                         pronundict=ttslab.fromfile(PRONUNDICT_FILE),
                         pronunaddendum=ttslab.fromfile(PRONUNADDENDUM_FILE),
                         synthesizer=SynthesizerUS(voice=None, unitcatalogue={}))
    ttslab.tofile(voice, "frontend.us.voice.pickle")

def us():
    from ttslab.defaultvoice import LwaziUSVoice
    from ttslab.synthesizer_us import SynthesizerUS
    voice = LwaziUSVoice(phoneset=ttslab.fromfile(PHONESET_FILE),
                         g2p=ttslab.fromfile(G2P_FILE),
                         pronundict=ttslab.fromfile(PRONUNDICT_FILE),
                         pronunaddendum=ttslab.fromfile(PRONUNADDENDUM_FILE),
                         synthesizer=SynthesizerUS(voice=None, unitcatalogue=ttslab.fromfile(USCATALOGUE_FILE)))
    ttslab.tofile(voice, "us.voice.pickle")

def wordusfrontend():
    from ttslab.defaultvoice import WordUSVoice
    from ttslab.synthesizer_us import SynthesizerUSWordUnits
    voice = WordUSVoice(phoneset=ttslab.fromfile(PHONESET_FILE),
                        g2p=ttslab.fromfile(G2P_FILE),
                        pronundict=ttslab.fromfile(PRONUNDICT_FILE),
                        pronunaddendum=ttslab.fromfile(PRONUNADDENDUM_FILE),
                        synthesizer=SynthesizerUSWordUnits(voice=None, unitcatalogue={}),
                        silword="PAUSE")
    ttslab.tofile(voice, "frontend.wordus.voice.pickle")

def wordus():
    from ttslab.defaultvoice import WordUSVoice
    from ttslab.synthesizer_us import SynthesizerUSWordUnits
    voice = WordUSVoice(phoneset=ttslab.fromfile(PHONESET_FILE),
                        g2p=ttslab.fromfile(G2P_FILE),
                        pronundict=ttslab.fromfile(PRONUNDICT_FILE),
                        pronunaddendum=ttslab.fromfile(PRONUNADDENDUM_FILE),
                        synthesizer=SynthesizerUSWordUnits(voice=None, unitcatalogue=ttslab.fromfile(USCATALOGUE_FILE)),
                        silword="PAUSE")
    ttslab.tofile(voice, "wordus.voice.pickle")

def htsfrontend():
    from ttslab.defaultvoice import LwaziHTSVoice
    from ttslab.synthesizer_htsme import SynthesizerHTSME
    voice = LwaziHTSVoice(phoneset=ttslab.fromfile(PHONESET_FILE),
                          g2p=ttslab.fromfile(G2P_FILE),
                          pronundict=ttslab.fromfile(PRONUNDICT_FILE),
                          pronunaddendum=ttslab.fromfile(PRONUNADDENDUM_FILE),
                          synthesizer=SynthesizerHTSME(voice=None, models_dir=None))
    ttslab.tofile(voice, "frontend.hts.voice.pickle")

def hts():
    from ttslab.defaultvoice import LwaziHTSVoice
    from ttslab.synthesizer_htsme import SynthesizerHTSME
    voice = LwaziHTSVoice(phoneset=ttslab.fromfile(PHONESET_FILE),
                          g2p=ttslab.fromfile(G2P_FILE),
                          pronundict=ttslab.fromfile(PRONUNDICT_FILE),
                          pronunaddendum=ttslab.fromfile(PRONUNADDENDUM_FILE),
                          synthesizer=SynthesizerHTSME(voice=None, models_dir=os.path.join(os.getcwd(), HTSMODELS_DIR)))
    ttslab.tofile(voice, "hts.voice.pickle")

def multihtsfrontend():
    from ttslab.defaultvoice import LwaziMultiHTSVoice
    from ttslab.synthesizer_htsme import SynthesizerHTSME
    try:
        voice = LwaziMultiHTSVoice(phoneset=ttslab.fromfile(PHONESET_FILE),
                                   g2p=ttslab.fromfile(G2P_FILE),
                                   pronundict=ttslab.fromfile(PRONUNDICT_FILE),
                                   pronunaddendum=ttslab.fromfile(PRONUNADDENDUM_FILE),
                                   engphoneset=ttslab.fromfile(ENGPHONESET_FILE),
                                   engg2p=ttslab.fromfile(ENGG2P_FILE),
                                   engpronundict=ttslab.fromfile(ENGPRONUNDICT_FILE),
                                   engpronunaddendum=ttslab.fromfile(ENGPRONUNADDENDUM_FILE),
                                   synthesizer=SynthesizerHTSME(voice=None, models_dir=None))
    except IOError:
        voice = LwaziMultiHTSVoice(phoneset=ttslab.fromfile(PHONESET_FILE),
                                   g2p=ttslab.fromfile(G2P_FILE),
                                   pronundict=ttslab.fromfile(PRONUNDICT_FILE),
                                   pronunaddendum=ttslab.fromfile(PRONUNADDENDUM_FILE),
                                   engphoneset=ttslab.fromfile(ENGPHONESET_FILE),
                                   engg2p=ttslab.fromfile(ENGG2P_FILE),
                                   engpronundict=ttslab.fromfile(ENGPRONUNDICT_FILE),
                                   engpronunaddendum={},
                                   synthesizer=SynthesizerHTSME(voice=None, models_dir=None))
    ttslab.tofile(voice, "frontend.multihts.voice.pickle")

def multihts():
    from ttslab.defaultvoice import LwaziMultiHTSVoice
    from ttslab.synthesizer_htsme import SynthesizerHTSME
    try:
        voice = LwaziMultiHTSVoice(phoneset=ttslab.fromfile(PHONESET_FILE),
                                   g2p=ttslab.fromfile(G2P_FILE),
                                   pronundict=ttslab.fromfile(PRONUNDICT_FILE),
                                   pronunaddendum=ttslab.fromfile(PRONUNADDENDUM_FILE),
                                   engphoneset=ttslab.fromfile(ENGPHONESET_FILE),
                                   engg2p=ttslab.fromfile(ENGG2P_FILE),
                                   engpronundict=ttslab.fromfile(ENGPRONUNDICT_FILE),
                                   engpronunaddendum=ttslab.fromfile(ENGPRONUNADDENDUM_FILE),
                                   synthesizer=SynthesizerHTSME(voice=None, models_dir=os.path.join(os.getcwd(), HTSMODELS_DIR)))
    except IOError:
        voice = LwaziMultiHTSVoice(phoneset=ttslab.fromfile(PHONESET_FILE),
                                   g2p=ttslab.fromfile(G2P_FILE),
                                   pronundict=ttslab.fromfile(PRONUNDICT_FILE),
                                   pronunaddendum=ttslab.fromfile(PRONUNADDENDUM_FILE),
                                   engphoneset=ttslab.fromfile(ENGPHONESET_FILE),
                                   engg2p=ttslab.fromfile(ENGG2P_FILE),
                                   engpronundict=ttslab.fromfile(ENGPRONUNDICT_FILE),
                                   engpronunaddendum={},
                                   synthesizer=SynthesizerHTSME(voice=None, models_dir=os.path.join(os.getcwd(), HTSMODELS_DIR)))
    ttslab.tofile(voice, "multihts.voice.pickle")


def frontend():
    from ttslab.defaultvoice import LwaziVoice
    voice = LwaziVoice(phoneset=ttslab.fromfile(PHONESET_FILE),
                       g2p=ttslab.fromfile(G2P_FILE),
                       pronundict=ttslab.fromfile(PRONUNDICT_FILE),
                       pronunaddendum=ttslab.fromfile(PRONUNADDENDUM_FILE))
    ttslab.tofile(voice, "frontend.voice.pickle")


if __name__ == "__main__":
    try:
        switches = ["frontend", "usfrontend", "htsfrontend", "wordusfrontend", "us", "wordus", "hts", "multihtsfrontend", "multihts"]
        switch = sys.argv[1]
        assert switch in switches
    except IndexError:
        print("USAGE: ttslab_make_voice.py [%s]" % "|".join(switches))
        sys.exit(1)
    
    if switch == "frontend":
        frontend()
    elif switch == "usfrontend":
        usfrontend()
    elif switch == "us":
        us()
    elif switch == "wordusfrontend":
        wordusfrontend()
    elif switch == "wordus":
        wordus()
    elif switch == "htsfrontend":
        htsfrontend()
    elif switch == "hts":
        hts()
    elif switch == "multihtsfrontend":
        multihtsfrontend()
    elif switch == "multihts":
        multihts()
    else:
        raise NotImplementedError
