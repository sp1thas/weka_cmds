# -*- coding: utf-8 -*-
# this file setups the working directory, weka, and filename
import os, termcolor

def classpath(working_dir):
    termcolor.cprint(''' ‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒
 _      __        __
| | /| / / ___   / /__ ___ _
| |/ |/ / / -_) /  '_// _ `/
|__/|__/  \__/_/_/\_\ \_,_/                 _             __    _
 / ___/ ___ _ / /_ ___   ___ _ ___   ____  (_) ___ ___ _ / /_  (_) ___   ___
/ /__  / _ `// __// -_) / _ `// _ \ / __/ / / /_ // _ `// __/ / / / _ \ / _ \\
\___/__\_,_/ \__/ \__/  \_, / \___//_/   /_/_ /__/\_,_/ \__/ /_/  \___//_//_/
 / ___/ ___   __ _   __/___/__ _ ___  ___/ / ___                /hdNdy/.
/ /__  / _ \ /  ' \ /  ' \/ _ `// _ \/ _  / (_-<              -hNMMMMMMNhs+
\___/  \___//_/_/_//_/_/_/\_,_//_//_/\_,_/ /___/      `:ohdNNNNMMMMMMmoo/o/
                                                   -odNNMMMMMMMMMMMMNy
   This project is licensed under the           :hNNMMMMMMMMMMMMMMMMMm.
   GNU General Public License version 3        oNMMMMMMMMMMMMMMMMMMMNy`
                                             .yNMMMMMMMMMMMMMMMMNNmo-
   Author: Simakis Panagiotis               sNNmy//sdMMMMMMMNNMNs`
   mailto:sp1thas@autistici.org             dy/`     /o+smNs-.ydm-
                                                         /dy   omo
   URL: https://git.io/vMqU5                             -mNysso:
 ‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒‒./hmNd:‒‒‒‒‒‒‒‒‒‒‒‒''',"blue", attrs=['bold'])
    return 'export CLASSPATH=$CLASSPATH:'+ working_dir
