#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x89EFD588E975D6DF (rbtcollins@hp.com)
#
Name     : testscenarios
Version  : 0.5.0
Release  : 40
URL      : https://pypi.python.org/packages/source/t/testscenarios/testscenarios-0.5.0.tar.gz
Source0  : https://pypi.python.org/packages/source/t/testscenarios/testscenarios-0.5.0.tar.gz
Source99 : https://pypi.python.org/packages/source/t/testscenarios/testscenarios-0.5.0.tar.gz.asc
Summary  : Testscenarios, a pyunit extension for dependency injection
Group    : Development/Tools
License  : Apache-2.0
Requires: testscenarios-python3
Requires: testscenarios-license
Requires: testscenarios-python
Requires: pbr
Requires: testtools
BuildRequires : Babel-legacypython
BuildRequires : extras
BuildRequires : pbr
BuildRequires : pbr-legacypython
BuildRequires : pip
BuildRequires : py
BuildRequires : pytest
BuildRequires : python-core
BuildRequires : python3-core
BuildRequires : python3-dev
BuildRequires : pytz-legacypython
BuildRequires : setuptools
BuildRequires : setuptools-legacypython
BuildRequires : testtools
BuildRequires : traceback2

%description
*****************************************************************
testscenarios: extensions to python unittest to support scenarios
*****************************************************************

%package doc
Summary: doc components for the testscenarios package.
Group: Documentation

%description doc
doc components for the testscenarios package.


%package legacypython
Summary: legacypython components for the testscenarios package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the testscenarios package.


%package license
Summary: license components for the testscenarios package.
Group: Default

%description license
license components for the testscenarios package.


%package python
Summary: python components for the testscenarios package.
Group: Default
Requires: testscenarios-python3

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
export SOURCE_DATE_EPOCH=1530377751
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1530377751
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/testscenarios
cp Apache-2.0 %{buildroot}/usr/share/doc/testscenarios/Apache-2.0
cp COPYING %{buildroot}/usr/share/doc/testscenarios/COPYING
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/testscenarios/*

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files license
%defattr(-,root,root,-)
/usr/share/doc/testscenarios/COPYING

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
