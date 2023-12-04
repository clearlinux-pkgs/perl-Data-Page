#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Data-Page
Version  : 2.03
Release  : 23
URL      : https://cpan.metacpan.org/authors/id/E/ET/ETHER/Data-Page-2.03.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/ET/ETHER/Data-Page-2.03.tar.gz
Summary  : 'help when paging through sets of results'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Data-Page-license = %{version}-%{release}
Requires: perl-Data-Page-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Class::Accessor::Chained::Fast)
BuildRequires : perl(Sub::Uplevel)
BuildRequires : perl(Test::Exception)

%description
This archive contains the distribution Data-Page,
version 2.03:
help when paging through sets of results

%package dev
Summary: dev components for the perl-Data-Page package.
Group: Development
Provides: perl-Data-Page-devel = %{version}-%{release}
Requires: perl-Data-Page = %{version}-%{release}

%description dev
dev components for the perl-Data-Page package.


%package license
Summary: license components for the perl-Data-Page package.
Group: Default

%description license
license components for the perl-Data-Page package.


%package perl
Summary: perl components for the perl-Data-Page package.
Group: Default
Requires: perl-Data-Page = %{version}-%{release}

%description perl
perl components for the perl-Data-Page package.


%prep
%setup -q -n Data-Page-2.03
cd %{_builddir}/Data-Page-2.03

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Data-Page
cp %{_builddir}/Data-Page-2.03/LICENCE %{buildroot}/usr/share/package-licenses/perl-Data-Page/f308a3e844152dba82d6236a97b349268414e231
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Data::Page.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Data-Page/f308a3e844152dba82d6236a97b349268414e231

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
