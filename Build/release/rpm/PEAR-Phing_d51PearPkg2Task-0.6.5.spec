%define peardir %(pear config-get php_dir 2> /dev/null || echo %{_datadir}/pear)
%define xmldir  /var/lib/pear

Summary: PEAR: An alternative to phing's default pearpkg2
Name: PEAR-Phing_d51PearPkg2Task
Version: 0.6.5
Release: 1
License: LGPL
Group: Development/Libraries
Source0: http://pear.php.net/get/Phing_d51PearPkg2Task-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-root-%(%{__id_u} -n)
URL: http://pear.php.net/package/Phing_d51PearPkg2Task
BuildRequires: php-pear >= 1.4.7
Requires: PEAR-PEAR_PackageFileManager2 >= 1.0.1
Requires: php-pear >= 1.6.0
BuildArch: noarch

%description
This package provides an alternative to phing's
                bundled pearpkg2, allowing for a build script 
                that more closely resembles a real 
                package.xml 2.0 file or using the API that is 
                available by using PEAR_PackageFileManager2.

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
cp -p package.xml %{buildroot}%{xmldir}/Phing_d51PearPkg2Task.xml

%clean
rm -rf %{buildroot}

%post
pear install --nodeps --soft --force --register-only %{xmldir}/Phing_d51PearPkg2Task.xml

%postun
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only pear.php.net/Phing_d51PearPkg2Task
fi

%files
%defattr(-,root,root)

%{peardir}/*
%{xmldir}/Phing_d51PearPkg2Task.xml
