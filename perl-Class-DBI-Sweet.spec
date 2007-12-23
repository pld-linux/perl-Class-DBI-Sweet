#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Class
%define	pnam	DBI-Sweet
Summary:	Class::DBI::Sweet - Making sweet things sweeter
Summary(pl.UTF-8):	Class::DBI::Sweet - czynienie miłych rzeczy milszymi
Name:		perl-Class-DBI-Sweet
Version:	0.08
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Class/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	7bdb32183faaff635e1c68f4e3c0396a
URL:		http://search.cpan.org/dist/Class-DBI-Sweet/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Cache-Cache
BuildRequires:	perl-Class-Accessor-Chained
BuildRequires:	perl-Class-DBI >= 0.96
BuildRequires:	perl-DBD-SQLite >= 1.08
BuildRequires:	perl-Data-Page
BuildRequires:	perl-Data-UUID
BuildRequires:	perl-SQL-Abstract
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Class::DBI::Sweet provides convenient count, search, page, and cache
functions in a sweet package. It integrates these functions with
Class::DBI in a convenient and efficient way.

%description -l pl.UTF-8
Class::DBI::Sweet dostarcza wygodne funkcje count, search, page i
chage w miłym pakiecie. Integruje te funkcje z Class::DBI w wygodny i
wydajny sposób.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	installdirs=vendor \
	destdir=$RPM_BUILD_ROOT
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Class/DBI/*.pm
%{perl_vendorlib}/Class/DBI/Sweet
%{_mandir}/man3/*
