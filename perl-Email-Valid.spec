%define module      Email-Valid
%define name        perl-%{module}
%define version     0.17.9
%define revision    0.179
%define release     %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Check validity of Internet email addresses
License:        GPL or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%module/
Source:         http://www.cpan.org/modules/by-module/Email/%{module}-%{revision}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:  perl-devel >= 0:5.600
%endif
BuildRequires:  perl(Mail::Address)
BuildRequires:  perl(Net::DNS)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
This module determines whether an email address is well-formed, and
optionally, whether a mail host exists for the domain or whether
the top level domain of the email address is valid.  

%prep
%setup -q -n %{module}-%{revision}

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


