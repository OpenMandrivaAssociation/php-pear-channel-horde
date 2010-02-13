%define peardir %(pear config-get php_dir 2> /dev/null || echo %{_datadir}/pear)
%define pear_xmldir  /var/lib/pear

Name:           php-pear-channel-horde
Version:        1.0
Release:        %mkrel 2
Summary:        Adds pear.horde.org channel to PEAR
Group:          Development/Languages
License:        BSD
URL:            http://pear.horde.org/
Source0:        http://pear.horde.org/channel.xml
BuildArch:      noarch
BuildRequires:  php-pear >= 5.1.1
PreReq:         php php-pear >= 5.1.1

%description
This package adds the pear.horde.org channel which allows PEAR packages
from this channel to be installed.


%prep
%setup -q -c -T


%build
# Empty build section, nothing to build


%install

%{__mkdir_p} %{buildroot}%{pear_xmldir}
%{__install} -pm 644 %{SOURCE0} %{buildroot}%{pear_xmldir}/pear.horde.org.xml


%clean

%{__rm} -rf %{buildroot}


%post

if [ $1 -eq  1 ] ; then
   pear channel-add %{pear_xmldir}/pear.horde.org.xml > /dev/null || :
else
   pear channel-update %{pear_xmldir}/pear.horde.org.xml > /dev/null ||:
fi


%postun

if [ $1 -eq 0 ] ; then
   pear channel-delete pear.horde.org.xml > /dev/null || :
fi


%files
%defattr(-,root,root,-)
%{pear_xmldir}/pear.horde.org.xml


