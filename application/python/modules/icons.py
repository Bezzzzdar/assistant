from dataclasses import dataclass

import base64
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon, QPixmap, QImage

@dataclass(slots=True, frozen=True)
class Base64ConstIcons():
    base64_side_bar_logo: str = """
        iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAACXBIWXMAAAsTAAALEwEAmpwYAAADKUlEQVR4nO2ZS2
        yMURTHbx9RVCORTNrYNJFGQ3SBeCwIaUJj01VFV8TGxsqeeG5QCZGmNpYikUpEUlYIk1BFlWpaFoJGiVcoiwbJTy7n
        cjPm8X3jnslXmX/yJTN3zvf/n3Of554xpoxoAK4Dd8x0BwIz3UE5kIThfxqRNHDDJAHALuAikCqhZgo4D+wMSXpBZs
        gwUB+MOLdevWhZ9IbuHUc8AjTksKsAlgMHgGvAGPBFnlFp2w8sy6PVIBqu41IaveQEhrIEsAV4THRY28323QyuB16H
        6Yy+9NYQ0O+1NQEDnoPPgBPARqAZqJXHfm6T36yNQz+wwOO7DdzPNepaga0F3ohD48AOoCrCe5UyGk/l3fdAa2m8/t
        uZVuCrOHIOmF0Ehx2pXuGwXOt1vM3tQJP0osWRzHkek8uury7heudPM1WI8IA3EhWBON3I3ArBGUXU7k4Wz4uZTgWm
        2Qvh7gjFm6/n3Ba7TYF/u3CPqo6KHHZui61U4K+SkbZYGprfFzooIscVNU6Kxj6jKGJTDIs2RY1NonHFKIo8EZEmRY
        1m0RgrlmBORurgkPZsJqWtLqTzGX7UicZkVL+iBvL7UgRMSVuNYiA1ojEV1a9iRFxepXYn4VdiavHaKIrYU9dijXIi
        anHTKIp0/5SAvYoae0Sj2yiKtIvIiKLGsGi0G+WF6NbJKsXM4a3mhuLEdotYOnQ+xJ8DV+9U98RmefnQ1oC8nd5Nsz
        YUbyHRDhH9DCwOwLcQ+CScnWG8jC7eI8K25DPvH3jmAo+E63RYL6MvfFsBQf4Dib04gRnAVeG4Z6etjrfZT9279mD0
        al2uEnI2zuKXS9oZedfeDOdL+yDwUK0clFGgG3ROA4uAD3F3G2sr73wEWrz2IXdWBU+FCpVMgXXANynpLInA1yL234
        ENJSuZApc94qy9BBwWm54IfKfEtitCEftSiBgc8SGgL1/vAI3ER2OBWdBnr9em1IgbhUkqKAeSMOBNGZsdy9cV+eym
        QyCr5evKfHaJBPAqxjJ5aZIK4FiMQI6apAKYKcFM5AlgQv4P0b0BhgJQLQfpuDz2c3UwgTJMsvEDHSW6Nwb7oTcAAA
        AASUVORK5CYII=
    """

    base64_side_bar_icon: str = """
        iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAZ0lEQVR4nO3WwQ
        mAQAwF0SlPt/+zC4t9RGxAZRH84DzIPTkEBiRJek8DOlDh04H16pARsGQ9nP0Xh6zAFrBk3cy54zL7P5IkSR9pZjxZ
        9TsCyrbMeEmSpGzNjCerfkdAnpcZL0kScw7zFAKxsVXx1wAAAABJRU5ErkJggg==
    """
    base64_side_bar_hover_icon: str = """
        iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAcElEQVR4nO3YQQ
        qAMAxE0TlZsrXef21BvMeIB5AKFlvkP8g+swgMkQAA6CTkNeSasmeekGvI5TZIyvvoJfN5mOP/QUIuKW+jl8z2XDsu
        r28JAADgQ0GN91ztN6nxpsYDAAA0UONFjTffePGNBwComxMXbJKaX3uXHwAAAABJRU5ErkJggg==
    """

    base64_settings_icon: str = """
        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
    """

    base64_account_icon: str = """
        iVBORw0KGgoAAAANSUhEUgAAADAAAAAwCAYAAABXAvmHAAAACXBIWXMAAAsTAAALEwEAmpwYAAAEgklEQVR4nO2Z24
        tWVRjGN46jDR2cUaEigyI7QjYWGd2khQVpU4FSVNCfYNkB76aCojQ1O0jnqG4l8yKzuq7oQMbkTBJJF2VZWWlWUs7g
        Lx56Nq22e+9vrW/2N9PFPLDh+/Z63+d9915rvYe1s2wKU5h8ADOBK4EHgNeBz4FfgCPAX/494jHJLJFONtkALgaeBQ
        6QDuk8AyycDMcXAjsKDu0E1gMrgQVAH9Dtq8/3NLYB+DTQOwps1/hEON4DbALGbPxXYC1wbhtc5wHrgEPmGvXDHdcp
        588BhmxMa/tRoLcB3j47rgfAszO/Ga//NbII2G8DI52YbuAiYLdt/Ahc2qTzv5l4K3B8I8Tltk4AttnWoXE/hJdN/u
        ZfAroa87baZhfwcjAT88ezYYeCN9+VoHc38JHfoq4Pgbs0lvAQ24I9kb6xHW3yNR+1bIALgK9qYv+Xij4Jy2m39Ta0
        E+fHHG2iNixwuqdc+AS4DjgROAkYCGL/D8C8SM5+R6fRpMARJKl1CTrvWGd7WZmgZRDw7kjg3WidN1LKgzxJ9SZEKu
        EnxfUauTmui4RLIrlnex8pY/fHKKi2EdbGGLDOI7Ez5qQlPJTArxJFeDqmqswLs+jyIFgayyJkB/KllsXzKzgIPwMz
        6gRVEgs7Y8mt94H1LouQvdyy7yfa+Mx6V9QJqVYX1ieS5zOwvBMzUNjM92VVCJLHykqhcr2HE/ZA7siDiTZust7WOi
        F1UsKFieSLgjU6u0UUOpAShQrFnjCcVcFhkDonanTftu6bNXngrXaWjwDMte7+rAruX6nd6XGZWFn3emCWrxuCuup7
        4LQ2+Gda/886ocMWiiq6SvTPB/ZQjS/a6d6CIlE4nFUB2Guh5DdUMLTaFaiy+UGH2TvH0y4C8+zbN3VCuyzU+QY7Ef
        xT2AlDdUKq+4Xbsv8ZgNvt25Y6oTUWeqINAzo+We5m/z3ga+APX/r9rk8hlgHT2+B/yr7dWye02EK7EohV798PfEc8
        vgUG1S8k2FFj1bKU6A5CYX9kdpQzOUZcjiz1puvxpRB7tcfyZCnsjcn6QYmvZqi7lfDjFn6sRc+at5w44ixp5UihaF
        TPnGNjXc+tJd3Kp+JuV/PwO3BKhfP5ZlfLuQqYFut8wDMNuCM40NpSxgOc6n10NDo6Aq+ZdHPJ2JMeU4xfnOp4Cd9V
        wbnTppLxzS2jT0VGVVN/sHD/ZpOp5Fg6XudzANd4NinuCSfC0eQMDtwIrAj+9wL7bOSeJLI4e2uCCDUruL9CvjRhIG
        92Pu7ECR0w3Uf09U1Lm+Qzgrc/0Cj5sbOOc0pyRVwJZ1gcDU5ujLgART3biGpPUw951W3hmbi2MfL/viT1CtjW2VmT
        0Cmx2jkbUEx+ATijAd4zffItTlwRn9WM18ca63HWzD8xKfS9EnViVn7++mqQyMZ8gNWZT0wF4wtKPvKprnkRuMXZfE
        7wkW+u793qt503TgR9dNJBQlMPopOC54P9kQLpPCeOCXe85EG6/fF60B+zh4MP3Uf8e9hjg5atryqnMIVsQvA3mH2I
        Rtzui8AAAAAASUVORK5CYII=
    """

    base64_authors_icon: str = """
        iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAACXBIWXMAAAsTAAALEwEAmpwYAAADL0lEQVR4nO2ZzU
        sWURSHxzRTCzdhiwJTs0WbgiRQhEooIy2kRYuC+gNql+m2IPta1KKwbS4i0KKvZX4GUaTYOk1bFBUUomVRRPXExTtx
        OM37cceRed+YBwZe7pnze8/vzp079854XkJCQsJiANqAEeCLPYaB/V4+AVwgNWe9PLoSmdjn5TosDCefT8BJoMP+9h
        nych1gXhTcIdo7RftnL8+MdOazkUFZsDXQaX/7DHi5DtCS8VaHPV6uAWwErgJ94phLY2JOnXsFqI3bxArgDYvnNVAc
        p5FKoqMyTiMlwE9RzHM1bNId5lwfo1ESmxFrZkIUdM4h77zIe7G0VWYBcFcUdN8h74HIu+PFDdAlCpoKGHpmGPWaiU
        HFpkXeGS9ugMOioF/AShGrE7Gtor3MnutzKDYDPsAWNfvIgpcBp4FTQEEKg4bNXtzw78x1JIucozk1Y/mYnR9w0B6b
        vAyYc8T5+bVrTFgqgHJgl9muAjUR6tbYIWq0y6PSDfqj5cBF4LuacR4C6xehWwX0K81v9slfFLWJAuAWqXkLrA2hu8
        7mpqI3aiMHyMyNELo3s9Bti9LIbSH8zjz0gNVmbaWGQ6mDZpkapvespnlYvhftfVEaGRfCl0R7g+q9DQ6atSq3QcQu
        i/bxKI0MCOHH/k1o31f5/DY96qC52ub4tNv2IuCJaO+P0ki76r0J+y5XFvI0hO4z1RFDwKT6rxNRGlkFvCQ1Zr20PY
        TuDrVO00zK1XSYwnebvQXhmQ3aLdpng4mFZco8MF2MvCIa6oTmtog0p12MLKbXJM1CszkizVkXI6MicVAsuTMdcttr
        qBaa1SrW5aA7KPJGXYz0iMQRh7zjIu+r2SGq3aL5cuVzzEH3kci77mJEvjn/GBAvBSoC2q+JvLGA+JiIdwfEK4JWB6
        aGoE8V2RhpVcPgb9FAoZ2KfwD1aT7y9GS40sMqVm81zTOqULSvUbW0uBjR43mniBUDM7Z9r8r7EPRtJJsrbbRYYEa+
        BwaaVC1Vrsv2+VTj2e4hGlWb7rlWlytt4416b6Puu3n5NiZbM2nHc8D5TalmLNUBgVc6jW53qBkrISHh/+QPplPFIF
        y3cz0AAAAASUVORK5CYII=
    """

    base64_about_app_icon: str = """
        iVBORw0KGgoAAAANSUhEUgAAAEAAAABACAYAAACqaXHeAAAACXBIWXMAAAsTAAALEwEAmpwYAAACFklEQVR4nO3azY
        uNURgA8GdimMKI8rWZlVKDlSRZSGQsWKgRJYqkJGx8/AU2NjYsRFmJxkZiIbJgYSEsfEayIBtFCTGGn2732sjMPaMZ
        894z57e+p87zdN7nOe/z3oiiKIqiKIqiKIpRhmlYhm04gCM4hF3YiPmRG8zGYdzBd829wwWsRlu0KnTiGL76dw+xIl
        oNFuOFkfEDR6NVoLtxjEfa8ag6TMR9o2dTVBl2Gl1vMTWqCrcTA/mIG+jDvcTu8NvWqCq8TwjgFKb/pWjeTUzApagi
        tGGgyeb7hlg/Cx8SEvA8qkq9bw/mE7qarD+XkIDPUVXYMsimf2JPwvqTCQnojyrDZjxqbLb2SDxAb+LaawkJeBOtAB
        1oH8bvFyXUkJrLkRt04ak02yMnWFs71onBv8SkyAFm4Kx0tcvSysgBevB6GMEPZHP0sbvRFlPV3ix7IgfY0Hi/T1Wb
        DM2JHGACXg2j2K2LnGB5YvAXMSVygx0JwZ9v6UFoQvFrNiPojFxhVZMEnI6cqRfBx0P0+e7IHRbg2R/Bf6nVhxgv0N
        64Ce5tzA/mjvWeiuL/Dk57caVx23uCM1gYuVPvAoMNPb9Vet4/EhqfyIfSn20rVD/6KVOfE5EjzJTmVuRIfUKcMge4
        GrnCzYQE7ItcYWmTv8vUPqt1RM6wZpBh6HXMi/EAk7EeB7EfS8Z6T0VRFEVRFEVRxLjzC/vo2JrIKUgqAAAAAElFTk
        SuQmCC
    """

@dataclass
class Base64UserIcons():
    base64_profile_icon: str = """
        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
        gg==
    """

base64_const_icons = Base64ConstIcons()
base64_user_icons = Base64UserIcons()


def _get_icon_from_base64(base64_icon: str, width: int, height: int):
    """Function for decode image from base64 code"""
    image_data = base64.b64decode(base64_icon)
    image = QImage()
    image.loadFromData(image_data)
    pixmap = QPixmap.fromImage(image)
    icon_size = QSize(width, height)
    scaled_pixmap = pixmap.scaled(icon_size, Qt.KeepAspectRatio, Qt.SmoothTransformation)
    icon = QIcon(scaled_pixmap)

    return icon, icon_size