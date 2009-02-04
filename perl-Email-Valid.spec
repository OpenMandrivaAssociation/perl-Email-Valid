%define module      Email-Valid
%define name        perl-%{module}
%define up_version  0.180
%define version     %perl_convert_version %{up_version}
%define release     %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Check validity of Internet email addresses
License:        GPL or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%module/
Source:         http://www.cpan.org/modules/by-module/Email/%{module}-%{up_version}.tar.gz
BuildRequires:  perl(Mail::Address)
BuildRequires:  perl(Net::DNS)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
This module determines whether an email address is well-formed, and
optionally, whether a mail host exists for the domain or whether
the top level domain of the email address is valid.  

%prep
%setup -q -n %{module}-%{up_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/Email
%{_mandir}/*/*


