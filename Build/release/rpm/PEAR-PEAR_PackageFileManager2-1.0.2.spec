%define peardir %(pear config-get php_dir 2> /dev/null || echo %{_datadir}/pear)
%define xmldir  /var/lib/pear

Summary: PEAR: PEAR_PackageFileManager2 takes an existing v2 package.xml file and updates it with a new filelist and changelog
Name: PEAR-PEAR_PackageFileManager2
Version: 1.0.2
Release: 1
License: New BSD License
Group: Development/Libraries
Source0: http://pear.php.net/get/PEAR_PackageFileManager2-%{version}.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-root-%(%{__id_u} -n)
URL: http://pear.php.net/package/PEAR_PackageFileManager2
BuildRequires: php-pear >= 1.4.7
Requires: PEAR-PEAR_PackageFileManager_Plugins
Requires: php-pear >= 1.8.0
BuildArch: noarch

%description
This package revolutionizes the maintenance of PEAR packages.  With a few
parameters,
the entire v2 package.xml is automatically updated with a listing of all
files in a package.
Features include
 - manages the new package.xml 2.0 format in PEAR 1.4.0
 - can detect PHP and extension dependencies using PHP_CompatInfo
 - reads in an existing package.xml file, and only changes the
release/changelog
 - a plugin system for retrieving files in a directory.  Currently four
plugins
   exist, one for standard recursive directory content listing, one that
   reads the CVS/Entries files and generates a file listing based on the
contents
   of a checked out CVS repository, one that reads Subversion entries
files, and
   one that queries a Perforce repository.
 - incredibly flexible options for assigning install roles to
files/directories
 - ability to ignore any file based on a * ? wildcard-enabled string(s)
 - ability to include only files that match a * ? wildcard-enabled
string(s)
 - ability to manage dependencies
 - can output the package.xml in any directory, and read in the package.xml
   file from any directory.
 - can specify a different name for the package.xml file

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
cp -p package.xml %{buildroot}%{xmldir}/PEAR_PackageFileManager2.xml

%clean
rm -rf %{buildroot}

%post
pear install --nodeps --soft --force --register-only %{xmldir}/PEAR_PackageFileManager2.xml

%postun
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only pear.php.net/PEAR_PackageFileManager2
fi

%files
%defattr(-,root,root)
%doc docs/PEAR_PackageFileManager2/*
%{peardir}/*
%{xmldir}/PEAR_PackageFileManager2.xml
