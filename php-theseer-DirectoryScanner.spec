%define		status		stable
%define		pearname	DirectoryScanner
%define		php_min_version 5.1.2
%include	/usr/lib/rpm/macros.php
Summary:	%{pearname} - A recursive directory scanner and filter
Name:		php-theseer-DirectoryScanner
Version:	1.3.0
Release:	1
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.netpirates.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	13830bdf0ce1cf84bca273b1fe28c683
URL:		http://pear.netpirates.net/package/DirectoryScanner/
BuildRequires:	php-channel(pear.netpirates.net)
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php(fileinfo)
Requires:	php(spl)
Requires:	php-channel(pear.netpirates.net)
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A recursive directory scanner and filter

In PEAR status of this package is: %{status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/.channel.*/*.reg
%dir %{php_pear_dir}/TheSeer
%{php_pear_dir}/TheSeer/DirectoryScanner
