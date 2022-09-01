#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ibus-typing-booster
Version  : 2.18.10
Release  : 77
URL      : https://github.com/mike-fabian/ibus-typing-booster/releases/download/2.18.10/ibus-typing-booster-2.18.10.tar.gz
Source0  : https://github.com/mike-fabian/ibus-typing-booster/releases/download/2.18.10/ibus-typing-booster-2.18.10.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: ibus-typing-booster-bin = %{version}-%{release}
Requires: ibus-typing-booster-data = %{version}-%{release}
Requires: ibus-typing-booster-libexec = %{version}-%{release}
Requires: ibus-typing-booster-license = %{version}-%{release}
Requires: ibus-typing-booster-locales = %{version}-%{release}
Requires: m17n-lib
Requires: pypi-packaging
BuildRequires : gettext
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(ibus-1.0)
BuildRequires : pygobject
BuildRequires : pypi-packaging

%description
Ibus-typing-booster
Get faster typing experience by intelligent context sensitive completion.

%package bin
Summary: bin components for the ibus-typing-booster package.
Group: Binaries
Requires: ibus-typing-booster-data = %{version}-%{release}
Requires: ibus-typing-booster-libexec = %{version}-%{release}
Requires: ibus-typing-booster-license = %{version}-%{release}

%description bin
bin components for the ibus-typing-booster package.


%package data
Summary: data components for the ibus-typing-booster package.
Group: Data

%description data
data components for the ibus-typing-booster package.


%package libexec
Summary: libexec components for the ibus-typing-booster package.
Group: Default
Requires: ibus-typing-booster-license = %{version}-%{release}

%description libexec
libexec components for the ibus-typing-booster package.


%package license
Summary: license components for the ibus-typing-booster package.
Group: Default

%description license
license components for the ibus-typing-booster package.


%package locales
Summary: locales components for the ibus-typing-booster package.
Group: Default

%description locales
locales components for the ibus-typing-booster package.


%prep
%setup -q -n ibus-typing-booster-2.18.10
cd %{_builddir}/ibus-typing-booster-2.18.10

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1662071591
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make V=1 VERBOSE=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1662071591
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ibus-typing-booster
cp %{_builddir}/ibus-typing-booster-%{version}/COPYING %{buildroot}/usr/share/package-licenses/ibus-typing-booster/8624bcdae55baeef00cd11d5dfcfa60f68710a02 || :
%make_install
%find_lang ibus-typing-booster

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/emoji-picker

%files data
%defattr(-,root,root,-)
/usr/share/applications/emoji-picker.desktop
/usr/share/applications/ibus-setup-typing-booster.desktop
/usr/share/glib-2.0/schemas/org.freedesktop.ibus.engine.typing-booster.gschema.xml
/usr/share/ibus-typing-booster/data/UnicodeData.txt
/usr/share/ibus-typing-booster/data/annotations/af.xml
/usr/share/ibus-typing-booster/data/annotations/am.xml
/usr/share/ibus-typing-booster/data/annotations/ar.xml
/usr/share/ibus-typing-booster/data/annotations/ar_SA.xml
/usr/share/ibus-typing-booster/data/annotations/as.xml
/usr/share/ibus-typing-booster/data/annotations/ast.xml
/usr/share/ibus-typing-booster/data/annotations/az.xml
/usr/share/ibus-typing-booster/data/annotations/be.xml
/usr/share/ibus-typing-booster/data/annotations/bg.xml
/usr/share/ibus-typing-booster/data/annotations/bn.xml
/usr/share/ibus-typing-booster/data/annotations/br.xml
/usr/share/ibus-typing-booster/data/annotations/bs.xml
/usr/share/ibus-typing-booster/data/annotations/ca.xml
/usr/share/ibus-typing-booster/data/annotations/ccp.xml
/usr/share/ibus-typing-booster/data/annotations/ceb.xml
/usr/share/ibus-typing-booster/data/annotations/chr.xml
/usr/share/ibus-typing-booster/data/annotations/ckb.xml
/usr/share/ibus-typing-booster/data/annotations/cs.xml
/usr/share/ibus-typing-booster/data/annotations/cy.xml
/usr/share/ibus-typing-booster/data/annotations/da.xml
/usr/share/ibus-typing-booster/data/annotations/de.xml
/usr/share/ibus-typing-booster/data/annotations/de_CH.xml
/usr/share/ibus-typing-booster/data/annotations/doi.xml
/usr/share/ibus-typing-booster/data/annotations/dsb.xml
/usr/share/ibus-typing-booster/data/annotations/el.xml
/usr/share/ibus-typing-booster/data/annotations/en.xml
/usr/share/ibus-typing-booster/data/annotations/en_001.xml
/usr/share/ibus-typing-booster/data/annotations/en_AU.xml
/usr/share/ibus-typing-booster/data/annotations/en_CA.xml
/usr/share/ibus-typing-booster/data/annotations/en_GB.xml
/usr/share/ibus-typing-booster/data/annotations/en_IN.xml
/usr/share/ibus-typing-booster/data/annotations/es.xml
/usr/share/ibus-typing-booster/data/annotations/es_419.xml
/usr/share/ibus-typing-booster/data/annotations/es_MX.xml
/usr/share/ibus-typing-booster/data/annotations/es_US.xml
/usr/share/ibus-typing-booster/data/annotations/et.xml
/usr/share/ibus-typing-booster/data/annotations/eu.xml
/usr/share/ibus-typing-booster/data/annotations/fa.xml
/usr/share/ibus-typing-booster/data/annotations/ff.xml
/usr/share/ibus-typing-booster/data/annotations/ff_Adlm.xml
/usr/share/ibus-typing-booster/data/annotations/fi.xml
/usr/share/ibus-typing-booster/data/annotations/fil.xml
/usr/share/ibus-typing-booster/data/annotations/fo.xml
/usr/share/ibus-typing-booster/data/annotations/fr.xml
/usr/share/ibus-typing-booster/data/annotations/fr_CA.xml
/usr/share/ibus-typing-booster/data/annotations/ga.xml
/usr/share/ibus-typing-booster/data/annotations/gd.xml
/usr/share/ibus-typing-booster/data/annotations/gl.xml
/usr/share/ibus-typing-booster/data/annotations/gu.xml
/usr/share/ibus-typing-booster/data/annotations/ha.xml
/usr/share/ibus-typing-booster/data/annotations/ha_NE.xml
/usr/share/ibus-typing-booster/data/annotations/he.xml
/usr/share/ibus-typing-booster/data/annotations/hi.xml
/usr/share/ibus-typing-booster/data/annotations/hi_Latn.xml
/usr/share/ibus-typing-booster/data/annotations/hr.xml
/usr/share/ibus-typing-booster/data/annotations/hsb.xml
/usr/share/ibus-typing-booster/data/annotations/hu.xml
/usr/share/ibus-typing-booster/data/annotations/hy.xml
/usr/share/ibus-typing-booster/data/annotations/ia.xml
/usr/share/ibus-typing-booster/data/annotations/id.xml
/usr/share/ibus-typing-booster/data/annotations/ig.xml
/usr/share/ibus-typing-booster/data/annotations/is.xml
/usr/share/ibus-typing-booster/data/annotations/it.xml
/usr/share/ibus-typing-booster/data/annotations/ja.xml
/usr/share/ibus-typing-booster/data/annotations/jv.xml
/usr/share/ibus-typing-booster/data/annotations/ka.xml
/usr/share/ibus-typing-booster/data/annotations/kab.xml
/usr/share/ibus-typing-booster/data/annotations/kk.xml
/usr/share/ibus-typing-booster/data/annotations/kl.xml
/usr/share/ibus-typing-booster/data/annotations/km.xml
/usr/share/ibus-typing-booster/data/annotations/kn.xml
/usr/share/ibus-typing-booster/data/annotations/ko.xml
/usr/share/ibus-typing-booster/data/annotations/kok.xml
/usr/share/ibus-typing-booster/data/annotations/ku.xml
/usr/share/ibus-typing-booster/data/annotations/ky.xml
/usr/share/ibus-typing-booster/data/annotations/lb.xml
/usr/share/ibus-typing-booster/data/annotations/lo.xml
/usr/share/ibus-typing-booster/data/annotations/lt.xml
/usr/share/ibus-typing-booster/data/annotations/lv.xml
/usr/share/ibus-typing-booster/data/annotations/mai.xml
/usr/share/ibus-typing-booster/data/annotations/mi.xml
/usr/share/ibus-typing-booster/data/annotations/mk.xml
/usr/share/ibus-typing-booster/data/annotations/ml.xml
/usr/share/ibus-typing-booster/data/annotations/mn.xml
/usr/share/ibus-typing-booster/data/annotations/mni.xml
/usr/share/ibus-typing-booster/data/annotations/mr.xml
/usr/share/ibus-typing-booster/data/annotations/ms.xml
/usr/share/ibus-typing-booster/data/annotations/mt.xml
/usr/share/ibus-typing-booster/data/annotations/my.xml
/usr/share/ibus-typing-booster/data/annotations/nb.xml
/usr/share/ibus-typing-booster/data/annotations/ne.xml
/usr/share/ibus-typing-booster/data/annotations/nl.xml
/usr/share/ibus-typing-booster/data/annotations/nn.xml
/usr/share/ibus-typing-booster/data/annotations/no.xml
/usr/share/ibus-typing-booster/data/annotations/oc.xml
/usr/share/ibus-typing-booster/data/annotations/or.xml
/usr/share/ibus-typing-booster/data/annotations/pa.xml
/usr/share/ibus-typing-booster/data/annotations/pa_Arab.xml
/usr/share/ibus-typing-booster/data/annotations/pcm.xml
/usr/share/ibus-typing-booster/data/annotations/pl.xml
/usr/share/ibus-typing-booster/data/annotations/ps.xml
/usr/share/ibus-typing-booster/data/annotations/pt.xml
/usr/share/ibus-typing-booster/data/annotations/pt_PT.xml
/usr/share/ibus-typing-booster/data/annotations/qu.xml
/usr/share/ibus-typing-booster/data/annotations/rm.xml
/usr/share/ibus-typing-booster/data/annotations/ro.xml
/usr/share/ibus-typing-booster/data/annotations/root.xml
/usr/share/ibus-typing-booster/data/annotations/ru.xml
/usr/share/ibus-typing-booster/data/annotations/rw.xml
/usr/share/ibus-typing-booster/data/annotations/sa.xml
/usr/share/ibus-typing-booster/data/annotations/sat.xml
/usr/share/ibus-typing-booster/data/annotations/sc.xml
/usr/share/ibus-typing-booster/data/annotations/sd.xml
/usr/share/ibus-typing-booster/data/annotations/si.xml
/usr/share/ibus-typing-booster/data/annotations/sk.xml
/usr/share/ibus-typing-booster/data/annotations/sl.xml
/usr/share/ibus-typing-booster/data/annotations/so.xml
/usr/share/ibus-typing-booster/data/annotations/sq.xml
/usr/share/ibus-typing-booster/data/annotations/sr.xml
/usr/share/ibus-typing-booster/data/annotations/sr_Cyrl.xml
/usr/share/ibus-typing-booster/data/annotations/sr_Cyrl_BA.xml
/usr/share/ibus-typing-booster/data/annotations/sr_Latn.xml
/usr/share/ibus-typing-booster/data/annotations/sr_Latn_BA.xml
/usr/share/ibus-typing-booster/data/annotations/su.xml
/usr/share/ibus-typing-booster/data/annotations/sv.xml
/usr/share/ibus-typing-booster/data/annotations/sw.xml
/usr/share/ibus-typing-booster/data/annotations/sw_KE.xml
/usr/share/ibus-typing-booster/data/annotations/ta.xml
/usr/share/ibus-typing-booster/data/annotations/te.xml
/usr/share/ibus-typing-booster/data/annotations/tg.xml
/usr/share/ibus-typing-booster/data/annotations/th.xml
/usr/share/ibus-typing-booster/data/annotations/ti.xml
/usr/share/ibus-typing-booster/data/annotations/tk.xml
/usr/share/ibus-typing-booster/data/annotations/to.xml
/usr/share/ibus-typing-booster/data/annotations/tr.xml
/usr/share/ibus-typing-booster/data/annotations/tt.xml
/usr/share/ibus-typing-booster/data/annotations/ug.xml
/usr/share/ibus-typing-booster/data/annotations/uk.xml
/usr/share/ibus-typing-booster/data/annotations/ur.xml
/usr/share/ibus-typing-booster/data/annotations/uz.xml
/usr/share/ibus-typing-booster/data/annotations/vi.xml
/usr/share/ibus-typing-booster/data/annotations/wo.xml
/usr/share/ibus-typing-booster/data/annotations/xh.xml
/usr/share/ibus-typing-booster/data/annotations/yo.xml
/usr/share/ibus-typing-booster/data/annotations/yo_BJ.xml
/usr/share/ibus-typing-booster/data/annotations/yue.xml
/usr/share/ibus-typing-booster/data/annotations/yue_Hans.xml
/usr/share/ibus-typing-booster/data/annotations/zh.xml
/usr/share/ibus-typing-booster/data/annotations/zh_Hant.xml
/usr/share/ibus-typing-booster/data/annotations/zh_Hant_HK.xml
/usr/share/ibus-typing-booster/data/annotations/zu.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/af.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/am.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/ar.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/ar_SA.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/as.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/ast.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/az.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/be.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/bg.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/bn.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/br.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/bs.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/ca.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/ccp.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/ceb.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/chr.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/ckb.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/cs.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/cy.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/da.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/de.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/de_CH.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/doi.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/dsb.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/el.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/en.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/en_001.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/en_AU.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/en_CA.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/en_GB.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/en_IN.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/es.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/es_419.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/es_MX.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/es_US.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/et.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/eu.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/fa.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/ff.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/ff_Adlm.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/fi.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/fil.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/fo.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/fr.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/fr_CA.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/ga.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/gd.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/gl.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/gu.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/ha.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/ha_NE.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/he.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/hi.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/hi_Latn.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/hr.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/hsb.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/hu.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/hy.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/ia.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/id.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/ig.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/is.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/it.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/ja.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/jv.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/ka.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/kab.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/kk.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/kl.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/km.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/kn.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/ko.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/kok.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/ky.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/lb.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/lo.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/lt.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/lv.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/mai.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/mi.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/mk.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/ml.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/mn.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/mni.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/mr.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/ms.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/mt.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/my.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/nb.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/ne.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/nl.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/nn.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/no.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/oc.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/or.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/pa.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/pa_Arab.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/pcm.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/pl.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/ps.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/pt.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/pt_PT.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/qu.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/rm.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/ro.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/root.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/ru.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/rw.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/sa.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/sat.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/sc.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/sd.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/si.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/sk.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/sl.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/so.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/sq.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/sr.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/sr_Cyrl.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/sr_Cyrl_BA.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/sr_Latn.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/sr_Latn_BA.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/su.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/sv.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/sw.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/sw_KE.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/ta.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/te.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/tg.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/th.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/ti.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/tk.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/to.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/tr.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/tt.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/ug.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/uk.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/ur.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/uz.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/vi.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/wo.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/xh.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/yo.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/yo_BJ.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/yue.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/yue_Hans.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/zh.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/zh_Hant.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/zh_Hant_HK.xml
/usr/share/ibus-typing-booster/data/annotationsDerived/zu.xml
/usr/share/ibus-typing-booster/data/coin9.wav
/usr/share/ibus-typing-booster/data/emoji-data.txt
/usr/share/ibus-typing-booster/data/emoji-sequences.txt
/usr/share/ibus-typing-booster/data/emoji-test.txt
/usr/share/ibus-typing-booster/data/emoji-variation-sequences.txt
/usr/share/ibus-typing-booster/data/emoji-zwj-sequences.txt
/usr/share/ibus-typing-booster/data/emoji.json
/usr/share/ibus-typing-booster/data/fi_FI.dic
/usr/share/ibus-typing-booster/engine/emoji_picker.py
/usr/share/ibus-typing-booster/engine/factory.py
/usr/share/ibus-typing-booster/engine/hunspell_suggest.py
/usr/share/ibus-typing-booster/engine/hunspell_table.py
/usr/share/ibus-typing-booster/engine/itb_active_window.py
/usr/share/ibus-typing-booster/engine/itb_emoji.py
/usr/share/ibus-typing-booster/engine/itb_nltk.py
/usr/share/ibus-typing-booster/engine/itb_pango.py
/usr/share/ibus-typing-booster/engine/itb_util.py
/usr/share/ibus-typing-booster/engine/itb_version.py
/usr/share/ibus-typing-booster/engine/m17n_translit.py
/usr/share/ibus-typing-booster/engine/main.py
/usr/share/ibus-typing-booster/engine/tabsqlitedb.py
/usr/share/ibus-typing-booster/engine/tabstatistics.py
/usr/share/ibus-typing-booster/icons/ibus-typing-booster.svg
/usr/share/ibus-typing-booster/setup/i18n.py
/usr/share/ibus-typing-booster/setup/itb_version.py
/usr/share/ibus-typing-booster/setup/main.py
/usr/share/ibus-typing-booster/setup/pkginstall.py
/usr/share/ibus-typing-booster/setup/test_input_purpose.py
/usr/share/ibus/component/typing-booster.xml
/usr/share/icons/hicolor/128x128/apps/ibus-typing-booster.png
/usr/share/icons/hicolor/16x16/apps/ibus-typing-booster.png
/usr/share/icons/hicolor/22x22/apps/ibus-typing-booster.png
/usr/share/icons/hicolor/256x256/apps/ibus-typing-booster.png
/usr/share/icons/hicolor/32x32/apps/ibus-typing-booster.png
/usr/share/icons/hicolor/48x48/apps/ibus-typing-booster.png
/usr/share/icons/hicolor/64x64/apps/ibus-typing-booster.png
/usr/share/icons/hicolor/scalable/apps/ibus-typing-booster.svg
/usr/share/metainfo/emoji-picker.appdata.xml
/usr/share/metainfo/typing-booster.appdata.xml

%files libexec
%defattr(-,root,root,-)
/usr/libexec/ibus-engine-typing-booster
/usr/libexec/ibus-setup-typing-booster

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ibus-typing-booster/8624bcdae55baeef00cd11d5dfcfa60f68710a02

%files locales -f ibus-typing-booster.lang
%defattr(-,root,root,-)

