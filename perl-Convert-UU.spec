%include	/usr/lib/rpm/macros.perl
%define	pdir	Convert
%define	pnam	UU
Summary:	Convert::UU perl module
Summary(pl):	Modu� perla Convert::UU
Name:		perl-Convert-UU
Version:	0.40
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convert::UU - perl module for uuencode and uudecode.

%description -l pl
Convert::UU - modu� perla dla uuencode i uudecode.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/*
%{perl_sitelib}/Convert/UU.pm
%{_mandir}/man[13]/*
