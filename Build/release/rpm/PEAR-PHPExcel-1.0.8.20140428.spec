%define peardir %(pear config-get php_dir 2> /dev/null || echo %{_datadir}/pear)
%define xmldir  /var/lib/pear

Summary: PEAR: PHP Excel classes
Name: PEAR-PHPExcel
Version: 1.0.8.20140428
Release: 1
License: LGPL
Group: Development/Libraries
Source0: http://pear.php.net/get/PHPExcel-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-root-%(%{__id_u} -n)
URL: http://pear.php.net/package/PHPExcel
BuildRequires: php-pear >= 1.4.7
Requires: PEAR-Phing_d51PearPkg2Task

BuildArch: noarch

%description
Project providing a set of classes for the PHP programming language, which
allow you to write
                to Excel 2007 files and read from Excel 2007 files.

%prep
%setup -c -T
pear -v -c pearrc \
        -d php_dir=%{peardir} \
        -d doc_dir=/docs \
        -d bin_dir=%{_bindir} \
        -d data_dir=%{peardir}/data \
        -d test_dir=%{peardir}/tests \
        -d ext_dir=%{_libdir} \
        -s

%build

%install
rm -rf %{buildroot}
pear -c pearrc install --nodeps --packagingroot %{buildroot} %{SOURCE0}
        
# Clean up unnecessary files
rm pearrc
rm %{buildroot}/%{peardir}/.filemap
rm %{buildroot}/%{peardir}/.lock
rm -rf %{buildroot}/%{peardir}/.registry
rm -rf %{buildroot}%{peardir}/.channels
rm %{buildroot}%{peardir}/.depdb
rm %{buildroot}%{peardir}/.depdblock



# Install XML package description
mkdir -p %{buildroot}%{xmldir}
tar -xzf %{SOURCE0} package.xml
cp -p package.xml %{buildroot}%{xmldir}/PHPExcel.xml

%clean
rm -rf %{buildroot}

%post
pear install --nodeps --soft --force --register-only %{xmldir}/PHPExcel.xml

%postun
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only pear.php.net/PHPExcel
fi

%files
%defattr(-,root,root)

%{peardir}/*
%{xmldir}/PHPExcel.xml
