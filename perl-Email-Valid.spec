%define upstream_name     Email-Valid
%define upstream_version 1.193

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Check validity of Internet email addresses

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Email/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires: perl(Capture::Tiny)
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


