#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x89EFD588E975D6DF (rbtcollins@hp.com)
#
Name     : testscenarios
Version  : 0.5.0
Release  : 46
URL      : https://pypi.python.org/packages/source/t/testscenarios/testscenarios-0.5.0.tar.gz
Source0  : https://pypi.python.org/packages/source/t/testscenarios/testscenarios-0.5.0.tar.gz
Source99 : https://pypi.python.org/packages/source/t/testscenarios/testscenarios-0.5.0.tar.gz.asc
Summary  : Testscenarios, a pyunit extension for dependency injection
Group    : Development/Tools
License  : Apache-2.0
Requires: testscenarios-license = %{version}-%{release}
Requires: testscenarios-python = %{version}-%{release}
Requires: testscenarios-python3 = %{version}-%{release}
Requires: pbr
Requires: testtools
BuildRequires : buildreq-distutils3
BuildRequires : extras
BuildRequires : pbr
BuildRequires : py
BuildRequires : pytest
BuildRequires : testtools
BuildRequires : traceback2

%description
*****************************************************************
testscenarios: extensions to python unittest to support scenarios
*****************************************************************

%package license
Summary: license components for the testscenarios package.
Group: Default

%description license
license components for the testscenarios package.


%package python
Summary: python components for the testscenarios package.
Group: Default
Requires: testscenarios-python3 = %{version}-%{release}

%description python
python components for the testscenarios package.


%package python3
Summary: python3 components for the testscenarios package.
Group: Default
Requires: python3-core

%description python3
python3 components for the testscenarios package.


%prep
%setup -q -n testscenarios-0.5.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1554340817
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/testscenarios
cp Apache-2.0 %{buildroot}/usr/share/package-licenses/testscenarios/Apache-2.0
cp COPYING %{buildroot}/usr/share/package-licenses/testscenarios/COPYING
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/testscenarios/Apache-2.0
/usr/share/package-licenses/testscenarios/COPYING

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
