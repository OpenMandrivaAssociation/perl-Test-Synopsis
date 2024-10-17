%define upstream_name    Test-Synopsis
%define upstream_version 0.10

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Test your SYNOPSIS code
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/Test-Synopsis-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Filter::Util::Call)
BuildRequires:	perl(Test::Builder)
BuildArch:	noarch

%description
Test::Synopsis is an (author) test module to find .pm or .pod files under
your _lib_ directory and then make sure the example snippet code in your
_SYNOPSIS_ section passes the perl compile check.

Note that this module only checks the perl syntax (by wrapping the code
with 'sub') and doesn't actually run the code.

Suppose you have the following POD in your module.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.60.0-2mdv2011.0
+ Revision: 654319
- rebuild for updated spec-helper

* Sat Mar 27 2010 Jérôme Quelin <jquelin@mandriva.org> 0.60.0-1mdv2011.0
+ Revision: 528200
- import perl-Test-Synopsis


* Sat Mar 27 2010 cpan2dist 0.06-1mdv
- initial mdv release, generated with cpan2dist

