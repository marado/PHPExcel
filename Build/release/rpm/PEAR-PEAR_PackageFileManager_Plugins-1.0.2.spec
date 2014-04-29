%define peardir %(pear config-get php_dir 2> /dev/null || echo %{_datadir}/pear)
%define xmldir  /var/lib/pear

Summary: PEAR: The plugins for PEAR_PackageFileManager to pick up what files to use, supported are File, CVS, SVN, Perforce
Name: PEAR-PEAR_PackageFileManager_Plugins
Version: 1.0.2
Release: 1
License: New BSD License
Group: Development/Libraries
Source0: http://pear.php.net/get/PEAR_PackageFileManager_Plugins-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-root-%(%{__id_u} -n)
URL: http://pear.php.net/package/PEAR_PackageFileManager_Plugins
BuildRequires: php-pear >= 1.4.7
Requires: php-pear-XML-Serializer >= 0.19.0
Requires: php-pear >= 1.8.0
BuildArch: noarch

%description
The plugins for PEAR_PackageFileManager to pick up what files to use.
Supported are
* File
* CVS
* SVN
* Perforce

This package is to be used with PackageFileManager v1 and v2 and can't be
used on it's own

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

mv %{buildroot}/docs .


# Install XML package description
mkdir -p %{buildroot}%{xmldir}
tar -xzf %{SOURCE0} package.xml
cp -p package.xml %{buildroot}%{xmldir}/PEAR_PackageFileManager_Plugins.xml

%clean
rm -rf %{buildroot}

%post
pear install --nodeps --soft --force --register-only %{xmldir}/PEAR_PackageFileManager_Plugins.xml

%postun
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only pear.php.net/PEAR_PackageFileManager_Plugins
fi

%files
%defattr(-,root,root)
%doc docs/PEAR_PackageFileManager_Plugins/*
%{peardir}/*
%{xmldir}/PEAR_PackageFileManager_Plugins.xml
