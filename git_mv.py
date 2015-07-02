dirs = [
"./src/mobicoin-cli-res.rc",
"./src/mobicoin-cli.cpp",
"./src/mobicoind-res.rc",
"./src/mobicoind.cpp",
"./src/qt/locale/mobicoin_bar.ts",
"./src/qt/locale/mobicoin_bg.ts",
"./src/qt/locale/mobicoin_ca.ts",
"./src/qt/locale/mobicoin_cmn.ts",
"./src/qt/locale/mobicoin_cs.ts",
"./src/qt/locale/mobicoin_da.ts",
"./src/qt/locale/mobicoin_de.ts",
"./src/qt/locale/mobicoin_el.ts",
"./src/qt/locale/mobicoin_en.ts",
"./src/qt/locale/mobicoin_eo.ts",
"./src/qt/locale/mobicoin_es.ts",
"./src/qt/locale/mobicoin_fi.ts",
"./src/qt/locale/mobicoin_fr.ts",
"./src/qt/locale/mobicoin_hu_HU.ts",
"./src/qt/locale/mobicoin_it.ts",
"./src/qt/locale/mobicoin_lv_LV.ts",
"./src/qt/locale/mobicoin_nb.ts",
"./src/qt/locale/mobicoin_nl.ts",
"./src/qt/locale/mobicoin_pl.ts",
"./src/qt/locale/mobicoin_pt.ts",
"./src/qt/locale/mobicoin_pt_BR.ts",
"./src/qt/locale/mobicoin_ru.ts",
"./src/qt/locale/mobicoin_sk.ts",
"./src/qt/locale/mobicoin_sv.ts",
"./src/qt/locale/mobicoin_tr.ts",
"./src/qt/locale/mobicoin_vi.ts",
"./src/qt/locale/mobicoin_zh_CN.ts",
"./src/qt/locale/mobicoin_zh_HK.ts",
"./src/qt/mobicoin.cpp",
"./src/qt/mobicoin.qrc",
"./src/qt/mobicoinstrings.cpp",
"./src/qt/res/icons/mobicoin.icns",
"./src/qt/res/images/mobicoin_logo_horizontal.png",
"./src/qt/res/mobicoin-qt-res.rc",
"./src/test/test_mobicoin.cpp",
]

import os 

src = "mobicoin"
dst = "unpay"



for s in dirs:
	d = s.replace(src,dst)
	cmd = "git mv "+ s + " " + d
	print cmd
	os.system(cmd)


