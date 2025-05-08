Summary:	PAM module for using cryptographic tokens
Summary(pl.UTF-8):	Moduł PAM umożliwiający używanie tokenów kryptograficznych
Name:		pam-pam_p11
Version:	0.6.0
Release:	1
License:	LGPL v2.1+
Group:		Libraries
#Source0Download: https://github.com/OpenSC/pam_p11/releases
Source0:	https://github.com/OpenSC/pam_p11/releases/download/pam_p11-%{version}/pam_p11-%{version}.tar.gz
# Source0-md5:	72d8ba11240db31e284b7e64b0e232c1
URL:		https://github.com/OpenSC/pam_p11
BuildRequires:	gettext-tools >= 0.18.3
BuildRequires:	libp11-devel >= 0.2.4
BuildRequires:	openssl-devel >= 1.1.1
BuildRequires:	pam-devel
BuildRequires:	pkgconfig
Requires:	libp11 >= 0.2.4
Obsoletes:	pam-pam_opensc < 0.10
Obsoletes:	pam_opensc < 0.8.1-3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir		/%{_lib}

%description
pam_p11 is a plugable authentication module (PAM) package for using
cryptographic tokens such as smart cards and USB crypto tokens for
authentication.

%description -l pl.UTF-8
pam_p11 to moduł uwierzytelniający (PAM) umożliwiający
uwierzytelnianie przy użyciu tokenów kryptograficznych, takich jak
karty procesorowe i tokeny kryptograficzne USB.

%prep
%setup -q -n pam_p11-%{version}

%build
%configure \
	--disable-static \
	--disable-strict
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT/%{_lib}/security/*.la
# packaged as %doc
%{__rm} $RPM_BUILD_ROOT%{_docdir}/pam_p11/{NEWS,README.md}

%find_lang pam_p11

%clean
rm -rf $RPM_BUILD_ROOT

%files -f pam_p11.lang
%defattr(644,root,root,755)
%doc NEWS README.md
%attr(755,root,root) /%{_lib}/security/pam_p11.so
