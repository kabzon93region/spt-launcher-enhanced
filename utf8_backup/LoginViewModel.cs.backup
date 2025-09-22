using SPT.Launcher.Attributes;
using SPT.Launcher.Helpers;
using SPT.Launcher.MiniCommon;
using SPT.Launcher.Models;
using SPT.Launcher.Models.SPT;
using SPT.Launcher.Models.Launcher;
using SPT.Launcher.ViewModels.Dialogs;
using Avalonia.Controls.Notifications;
using ReactiveUI;
using Splat;
using System.Collections.ObjectModel;
using System.Reactive;
using System.Threading.Tasks;
using Avalonia.Threading;
using SPT.Launcher.Controllers;

namespace SPT.Launcher.ViewModels
{
    [RequireServerConnected]
    public class LoginViewModel : ViewModelBase
    {
        public ObservableCollection<ProfileInfo> ExistingProfiles { get; set; } = new ObservableCollection<ProfileInfo>();

        public LoginModel Login { get; set; } = new LoginModel();

        public ReactiveCommand<Unit, Unit> LoginCommand { get; set; }

        public LoginViewModel(IScreen Host, bool NoAutoLogin = false) : base(Host)
        {
            //setup reactive commands
            LoginCommand = ReactiveCommand.CreateFromTask(async () =>
            {
                AccountStatus status = await LoginWithRetry(Login);

                switch (status)
                {
                    case AccountStatus.OK:
                        {
                            if (LauncherSettingsProvider.Instance.UseAutoLogin && LauncherSettingsProvider.Instance.Server.AutoLoginCreds != Login)
                            {
                                LauncherSettingsProvider.Instance.Server.AutoLoginCreds = Login;
                            }

                            LauncherSettingsProvider.Instance.SaveSettings();
                            NavigateTo(new ProfileViewModel(HostScreen, LauncherSettingsProvider.Instance.AutoLaunchGame));
                            break;
                        }
                    case AccountStatus.LoginFailed:
                        {
                            // Create account if it doesn't exist
                            if (!string.IsNullOrWhiteSpace(Login.Username))
                            {
                                if (Login.Username.Length > 15)
                                {
                                    SendNotification(LocalizationProvider.Instance.registration_failed, LocalizationProvider.Instance.register_failed_name_limit, NotificationType.Error);
                                    return;
                                }
                                
                                var result = await ShowDialog(new RegisterDialogViewModel(null, Login.Username));

                                if (result != null && result is SPTEdition edition)
                                {
                                    AccountStatus registerResult = await RegisterWithRetry(Login.Username, Login.Password, edition.Name);

                                    switch (registerResult)
                                    {
                                        case AccountStatus.OK:
                                            {
                                                if (LauncherSettingsProvider.Instance.UseAutoLogin && LauncherSettingsProvider.Instance.Server.AutoLoginCreds != Login)
                                                {
                                                    LauncherSettingsProvider.Instance.Server.AutoLoginCreds = Login;
                                                }

                                                LauncherSettingsProvider.Instance.SaveSettings();
                                                SendNotification(LocalizationProvider.Instance.profile_created, Login.Username, NotificationType.Success);
                                                NavigateTo(new ProfileViewModel(HostScreen, LauncherSettingsProvider.Instance.AutoLaunchGame));
                                                break;
                                            }
                                        case AccountStatus.RegisterFailed:
                                            {
                                                SendNotification("", LocalizationProvider.Instance.registration_failed, NotificationType.Error);
                                                break;
                                            }
                                        case AccountStatus.NoConnection:
                                            {
                                                NavigateTo(new ConnectServerViewModel(HostScreen));
                                                break;
                                            }
                                        default:
                                            {
                                                SendNotification("", registerResult.ToString(), NotificationType.Error);
                                                break;
                                            }
                                    }

                                    return;
                                }
                            }

                            SendNotification("", LocalizationProvider.Instance.login_failed, NotificationType.Error);

                            break;
                        }
                    case AccountStatus.NoConnection:
                        {
                            NavigateTo(new ConnectServerViewModel(HostScreen));
                            break;
                        }
                }
            });

            //cache and touch background image
            var backgroundImage = Locator.Current.GetService<ImageHelper>("bgimage");

            ImageRequest.CacheBackgroundImage();

            backgroundImage.Touch();

            //handle auto-login
            if (LauncherSettingsProvider.Instance.UseAutoLogin && LauncherSettingsProvider.Instance.Server.AutoLoginCreds != null && !NoAutoLogin)
            {
                Login = LauncherSettingsProvider.Instance.Server.AutoLoginCreds;
                Dispatcher.UIThread.InvokeAsync(() =>
                {
                    LoginCommand.Execute();
                });
                return;
            }

            Task.Run(() =>
            {
                GetExistingProfiles();
            });
        }

        public void LoginProfileCommand(object parameter)
        {
            if (parameter == null) return;

            Task.Run(() =>
            {
                if (parameter is string username)
                {
                    Login.Username = username;
                    LoginCommand.Execute();
                }
            });
        }

        public async Task GetExistingProfiles()
        {
            await Task.Delay(200);
            
            ServerProfileInfo[] existingProfiles = AccountManager.GetExistingProfiles();

            if(existingProfiles != null)
            {
                ExistingProfiles.Clear();

                foreach(ServerProfileInfo profile in existingProfiles)
                {
                    ProfileInfo profileInfo = new ProfileInfo(profile);

                    ExistingProfiles.Add(profileInfo);

                    ImageRequest.CacheSideImage(profileInfo.Side);

                    ImageHelper sideImage = new ImageHelper() { Path = profileInfo.SideImage };
                    sideImage.Touch();

                    await Task.Delay(100);
                }
            }
        }

        /// <summary>
        /// Выполняет вход с повторными попытками при ошибках соединения
        /// </summary>
        private async Task<AccountStatus> LoginWithRetry(LoginModel login)
        {
            if (!LauncherSettingsProvider.Instance.EnableRetryConnection)
            {
                return await AccountManager.LoginAsync(login);
            }

            int attempts = LauncherSettingsProvider.Instance.RetryAttempts;
            int delay = LauncherSettingsProvider.Instance.RetryDelay * 1000; // конвертируем в миллисекунды

            for (int i = 0; i < attempts; i++)
            {
                AccountStatus status = await AccountManager.LoginAsync(login);

                // Если успешно или ошибка не связана с соединением - возвращаем результат
                if (status != AccountStatus.NoConnection)
                {
                    return status;
                }

                // Если это не последняя попытка - ждем и повторяем
                if (i < attempts - 1)
                {
                    LogManager.Instance.Info($"[Login] Попытка {i + 1} из {attempts} не удалась. Повтор через {delay / 1000} секунд...");
                    await Task.Delay(delay);
                }
            }

            // Все попытки исчерпаны
            LogManager.Instance.Warning($"[Login] Все {attempts} попыток входа исчерпаны. Соединение с сервером недоступно.");
            return AccountStatus.NoConnection;
        }

        /// <summary>
        /// Выполняет регистрацию с повторными попытками при ошибках соединения
        /// </summary>
        private async Task<AccountStatus> RegisterWithRetry(string username, string password, string edition)
        {
            if (!LauncherSettingsProvider.Instance.EnableRetryConnection)
            {
                return await AccountManager.RegisterAsync(username, password, edition);
            }

            int attempts = LauncherSettingsProvider.Instance.RetryAttempts;
            int delay = LauncherSettingsProvider.Instance.RetryDelay * 1000; // конвертируем в миллисекунды

            for (int i = 0; i < attempts; i++)
            {
                AccountStatus status = await AccountManager.RegisterAsync(username, password, edition);

                // Если успешно или ошибка не связана с соединением - возвращаем результат
                if (status != AccountStatus.NoConnection)
                {
                    return status;
                }

                // Если это не последняя попытка - ждем и повторяем
                if (i < attempts - 1)
                {
                    LogManager.Instance.Info($"[Register] Попытка {i + 1} из {attempts} не удалась. Повтор через {delay / 1000} секунд...");
                    await Task.Delay(delay);
                }
            }

            // Все попытки исчерпаны
            LogManager.Instance.Warning($"[Register] Все {attempts} попыток регистрации исчерпаны. Соединение с сервером недоступно.");
            return AccountStatus.NoConnection;
        }
    }
}
