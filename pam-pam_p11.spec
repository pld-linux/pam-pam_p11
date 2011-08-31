Summary:	PAM module for using cryptographic tokens
Summary(pl.UTF-8):	Moduł PAM umożliwiający używanie tokenów kryptograficznych
Name:		pam-pam_p11
Version:	0.1.5
Release:	4
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://www.opensc-project.org/files/pam_p11/pam_p11-%{version}.tar.gz
# Source0-md5:	94684503b075eef02e03aafaff5d4a55
URL:		http://www.opensc-project.org/pam_p11/
BuildRequires:	libp11-devel
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pam-devel
BuildRequires:	pkgconfig
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

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/pam_p11/*.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS doc/{ChangeLog,*.html,*.css}
%attr(755,root,root) /%{_lib}/security/pam_p11_opensc.so
%attr(755,root,root) /%{_lib}/security/pam_p11_openssh.so
