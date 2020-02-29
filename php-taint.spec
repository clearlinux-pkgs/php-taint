#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-taint
Version  : 2.0.6
Release  : 5
URL      : https://pecl.php.net/get/taint-2.0.6.tgz
Source0  : https://pecl.php.net/get/taint-2.0.6.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : PHP-3.01
Requires: php-taint-lib = %{version}-%{release}
BuildRequires : buildreq-php

%description
No detailed description available

%package lib
Summary: lib components for the php-taint package.
Group: Libraries

%description lib
lib components for the php-taint package.


%prep
%setup -q -n taint-2.0.6
cd %{_builddir}/taint-2.0.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure
make  %{?_smp_mflags}

%install
%make_install


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20190902/taint.so
