%define upstream_name     Email-Valid
%define upstream_version 1.192

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Check validity of Internet email addresses
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Email/Email-Valid-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Mail::Address)
BuildRequires:	perl(Net::DNS)
BuildArch:	noarch

%description
This module determines whether an email address is well-formed, and
optionally, whether a mail host exists for the domain or whether
the top level domain of the email address is valid.  

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/Email
%{_mandir}/*/*

%changelog
* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.184.0-1mdv2011.0
+ Revision: 552696
- update to 0.184

* Tue Aug 11 2009 Jérôme Quelin <jquelin@mandriva.org> 0.182.0-1mdv2010.0
+ Revision: 415002
- update to 0.182

* Sun May 17 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.181.0-1mdv2010.0
+ Revision: 376723
- new version
- new release
- standardized version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.17.9-3mdv2009.0
+ Revision: 256791
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 0.17.9-1mdv2008.1
+ Revision: 135841
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Jan 06 2007 Stefan van der Eijk <stefan@mandriva.org> 0.17.9-1mdv2007.0
+ Revision: 104731
- 0.17.9 / 0.179

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - Import perl-Email-Valid

* Thu Aug 03 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.17.6-1mdv2007.0
- new version (upstream version 0.176)

* Tue Jun 27 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.17.5-1mdv2007.0
- New version (upstream versop, 0.175)

* Thu Jun 22 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.17.4-1mdv2007.0
- New version (upstream version 0.174)

* Fri Jun 16 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.17.2-1mdv2007.0
- New version (upstream version 0.172)

* Wed Jun 14 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.17.1-1mdv2007.0
- New version (upstream version 0.171)

* Thu Jun 08 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.16-1mdv2007.0
- New release 0.16
- spec cleanup
- better URL
- better summary

* Sun Feb 05 2006 Stefan van der Eijk <stefan@eijk.nu> 0.15-4mdk
- Rebuild
- %%mkrel

* Mon Jan 17 2005 Stefan van der Eijk <stefan@mandrake.org> 0.15-3mdk
- add missing BuildRequires perl-Net-DNS

* Mon Jan 17 2005 Stefan van der Eijk <stefan@mandrake.org> 0.15-2mdk
- yearly rebuild



