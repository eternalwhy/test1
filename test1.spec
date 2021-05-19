%global srcname test1

Name:           python-%{srcname}
Version:        1.2.3
Release:        1%{?dist}
Summary:        Example python module

License:        MIT
URL:            https://github.com/eternalwhy/test1/
Source0:        %{pypi_source}

BuildArch:      noarch

%global _description %{expand:
test task}

%description %_description

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-%{srcname} %_description

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{python3} setup.py test1

# Note that there is no %%files section for the unversioned python module
%files -n python3-%{srcname}
%license COPYING
%doc README.rst
%{python3_sitelib}/%{srcname}-*.egg-info/
%{python3_sitelib}/%{srcname}/
%{_bindir}/sample-exec