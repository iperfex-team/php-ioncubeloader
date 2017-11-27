# PHP-IONCUBELOADER

iPERFEX (c) 2012-2017
 Federico Pereira <fpereira@iperfex.com>


## Introduction
PHP-IONCUBELOADER 

## Files
```bash
php-ioncubeloader/
php-ioncubeloader/setup/
php-ioncubeloader/setup/ioncubeloader/
php-ioncubeloader/setup/ioncubeloader/ioncube_loader_lin_5.5_ts.so
php-ioncubeloader/setup/ioncubeloader/ioncube_loader_lin_5.1_ts.so
php-ioncubeloader/setup/ioncubeloader/ioncube_loader_lin_5.2_ts.so
php-ioncubeloader/setup/ioncubeloader/ioncube_loader_lin_4.4.so
php-ioncubeloader/setup/ioncubeloader/ioncube_loader_lin_5.1.so
php-ioncubeloader/setup/ioncubeloader/ioncube_loader_lin_5.6.so
php-ioncubeloader/setup/ioncubeloader/ioncube_loader_lin_5.0_ts.so
php-ioncubeloader/setup/ioncubeloader/ioncube_loader_lin_4.3_ts.so
php-ioncubeloader/setup/ioncubeloader/ioncube_loader_lin_5.0.so
php-ioncubeloader/setup/ioncubeloader/ioncube_loader_lin_7.0.so
php-ioncubeloader/setup/ioncubeloader/ioncube_loader_lin_5.6_ts.so
php-ioncubeloader/setup/ioncubeloader/ioncube_loader_lin_5.3.so
php-ioncubeloader/setup/ioncubeloader/ioncube_loader_lin_4.1.so
php-ioncubeloader/setup/ioncubeloader/ioncube_loader_lin_4.4_ts.so
php-ioncubeloader/setup/ioncubeloader/ioncube_loader_lin_5.4_ts.so
php-ioncubeloader/setup/ioncubeloader/ioncube_loader_lin_5.4.so
php-ioncubeloader/setup/ioncubeloader/ioncube_loader_lin_7.0_ts.so
php-ioncubeloader/setup/ioncubeloader/ioncube_loader_lin_5.2.so
php-ioncubeloader/setup/ioncubeloader/ioncube_loader_lin_4.2.so
php-ioncubeloader/setup/ioncubeloader/ioncube_loader_lin_5.5.so
php-ioncubeloader/setup/ioncubeloader/ioncube_loader_lin_4.3.so
php-ioncubeloader/setup/ioncubeloader/ioncube_loader_lin_5.3_ts.so
```

## Installation

```bash
cd /usr/src
git clone https://github.com/iperfex-team/php-ioncubeloader.git
cd /usr/src/iperfex-agi/rpmbuild/SOURCES/
tar -czvf iperfex-agi_3.0.0-1.tgz iperfex-agi
yes | mv /usr/src/iperfex-agi/rpmbuild/SOURCES/iperfex-agi_3.0.0-1.tgz /root/rpmbuild/SOURCES/
yes | cp -fra /usr/src/iperfex-agi/rpmbuild/SPECS/iperfex-agi_3.0.0-1.spec /root/rpmbuild/SPECS/
rpmbuild -ba /root/rpmbuild/SPECS/php-ioncubeloader.spec
```

## Install
```bash
rpm -i /root/rpmbuild/RPMS/x86_64/php-ioncubeloader-3-0.0.0.x86_64.rpm
```

## Uninstall
```bash
rpm -e --nodeps php-ioncubeloader
```
Or
```bash
rpm -e --noscripts php-ioncubeloader-3-0.0.0
```
