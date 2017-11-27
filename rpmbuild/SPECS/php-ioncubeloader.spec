%define __os_install_post %{nil}
%define modname php-ioncubeloader

Summary: Ioncube Loader for PHP
Vendor: iPERFEX
Name: %{modname}
Version: 3
License: Commercial
Release: 0.0.0
Group: Applications/System
Source0: %{modname}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildArch: %{_arch}
Requires(pre): php
AutoReq: no

%description
Loader for encoded PHP Files

%prep
%setup -n %{modname}

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p                     $RPM_BUILD_ROOT/usr/local/ioncubeloader
mv setup/ioncubeloader/*     $RPM_BUILD_ROOT/usr/local/ioncubeloader

%preun

rm -f /etc/php.d/00-ioncube.ini
service httpd restart

%post

PHPVER=$(php -v | head -n1 | cut -d ' ' -f2 | awk -F. '{print $1"."$2}');
PHPSOFILE="zend_extension=/usr/local/ioncubeloader/ioncube_loader_lin_$PHPVER.so";

if [ $1 -eq 1 ]; then #install

    echo $PHPSOFILE > /etc/php.d/00-ioncube.ini;

    service httpd restart

fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/local/ioncubeloader
%changelog
