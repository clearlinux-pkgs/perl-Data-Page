#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Data-Page
Version  : 2.02
Release  : 7
URL      : https://cpan.metacpan.org/authors/id/L/LB/LBROCARD/Data-Page-2.02.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/L/LB/LBROCARD/Data-Page-2.02.tar.gz
Summary  : help when paging through sets of results
Group    : Development/Tools
License  : Artistic-1.0-Perl
BuildRequires : buildreq-cpan
BuildRequires : perl(Class::Accessor::Chained::Fast)
BuildRequires : perl(Sub::Uplevel)
BuildRequires : perl(Test::Exception)

%description
NAME
Data::Page - help when paging through sets of results
SYNOPSIS
use Data::Page;

%package dev
Summary: dev components for the perl-Data-Page package.
Group: Development
Provides: perl-Data-Page-devel = %{version}-%{release}

%description dev
dev components for the perl-Data-Page package.


%prep
%setup -q -n Data-Page-2.02

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
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
/usr/lib/perl5/vendor_perl/5.28.1/Data/Page.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Data::Page.3
