Summary:	PAM module for using cryptographic tokens
Summary(pl.UTF-8):	Moduł PAM umożliwiający używanie tokenów kryptograficznych
Name:		pam-pam_p11
Version:	0.2.0
Release:	3
License:	LGPL v2.1+
Group:		Libraries
#Source0Download: https://github.com/OpenSC/pam_p11/releases
Source0:	https://github.com/OpenSC/pam_p11/releases/download/pam_p11-%{version}/pam_p11-%{version}.tar.gz
# Source0-md5:	05ca327726120bd6cd31ac298691a762
Patch0:		openssl-1.1.1.patch
URL:		https://github.com/OpenSC/pam_p11
BuildRequires:	gettext-tools >= 0.18.3
BuildRequires:	libp11-devel >= 0.2.4
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pam-devel
BuildRequires:	pkgconfig
Requires:	libp11 >= 0.2.4
Obsoletes:	pam-pam_opensc
Obsoletes:	pam_opensc
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
%patch0 -p1

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
%{__rm} $RPM_BUILD_ROOT%{_docdir}/pam_p11/NEWS

%find_lang pam_p11

%clean
rm -rf $RPM_BUILD_ROOT

%files -f pam_p11.lang
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) /%{_lib}/security/pam_p11.so
